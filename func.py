def autoregressive_inference(params, ic, valid_data_full, model): 
    print(valid_data_full.shape)
    ic = int(ic) 
    #initialize global variables
    device = torch.cuda.current_device() if torch.cuda.is_available() else 'cpu'
    exp_dir = params['experiment_dir'] 
    dt = int(params.dt)
    prediction_length = int(params.prediction_length/dt)
    n_history = params.n_history
    img_shape_x = params.img_shape_x
    img_shape_y = params.img_shape_y
    in_channels = np.array(params.in_channels)
    out_channels = np.array(params.out_channels)
    n_in_channels = len(in_channels)
    n_out_channels = len(out_channels)
    means = params.means
    stds = params.stds

    #initialize memory for image sequences and RMSE/ACC
    valid_loss = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)
    acc = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)

    # compute metrics in a coarse resolution too if params.interp is nonzero
    valid_loss_coarse = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)
    acc_coarse = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)
    acc_coarse_unweighted = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)
    
    acc_unweighted = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)
    seq_real = torch.zeros((prediction_length, n_in_channels, img_shape_x, img_shape_y)).to(device, dtype=torch.float)
    seq_pred = torch.zeros((prediction_length, n_in_channels, img_shape_x, img_shape_y)).to(device, dtype=torch.float)

    acc_land = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)
    acc_sea = torch.zeros((prediction_length, n_out_channels)).to(device, dtype=torch.float)
    if params.masked_acc:
      maskarray = torch.as_tensor(np.load(params.maskpath)[0:720]).to(device, dtype=torch.float)

    valid_data = valid_data_full[ic:(ic+prediction_length*dt+n_history*dt):dt, in_channels, 0:720] #extract valid data from first year
    # standardize
    valid_data = (valid_data - means)/stds
    valid_data = torch.as_tensor(valid_data).to(device, dtype=torch.float)

    #load time means
    if not params.use_daily_climatology:
      m = torch.as_tensor((np.load(params.time_means_path)[0][out_channels] - means)/stds)[:, 0:img_shape_x] # climatology
      m = torch.unsqueeze(m, 0)
    else:
      # use daily clim like weyn et al. (different from rasp)
      dc_path = params.dc_path
      with h5py.File(dc_path, 'r') as f:
        dc = f['time_means_daily'][ic:ic+prediction_length*dt:dt] # 1460,21,721,1440
      m = torch.as_tensor((dc[:,out_channels,0:img_shape_x,:] - means)/stds) 

    m = m.to(device, dtype=torch.float)
    if params.interp > 0:
        m_coarse = downsample(m, scale=params.interp)

    std = torch.as_tensor(stds[:,0,0]).to(device, dtype=torch.float)

    orography = params.orography
    orography_path = params.orography_path
    if orography:
      orog = torch.as_tensor(np.expand_dims(np.expand_dims(h5py.File(orography_path, 'r')['orog'][0:720], axis = 0), axis = 0)).to(device, dtype = torch.float)
      logging.info("orography loaded; shape:{}".format(orog.shape))

    #autoregressive inference
    if params.log_to_screen:
      logging.info('Begin autoregressive inference')
    
    with torch.no_grad():
      for i in range(valid_data.shape[0]-1):
        if i==0: #start of sequence
          first = valid_data[0:n_history+1]
          future = valid_data[n_history+1]
          for h in range(n_history+1):
            seq_real[h] = first[h*n_in_channels : (h+1)*n_in_channels][0:n_out_channels] #extract history from 1st 
            seq_pred[h] = seq_real[h]
          if params.perturb:
            first = gaussian_perturb(first, level=params.n_level, device=device) # perturb the ic
          if orography:
            future_pred = model(torch.cat((first, orog), axis=1))
          else:
            future_pred = model(first)
        else:
          if i < prediction_length-1:
            future = valid_data[n_history+i+1]
          if orography:
            future_pred = model(torch.cat((future_pred, orog), axis=1)) #autoregressive step
          else:
            future_pred = model(future_pred) #autoregressive step

        if i < prediction_length-1: #not on the last step
          seq_pred[n_history+i+1] = future_pred
          seq_real[n_history+i+1] = future
          history_stack = seq_pred[i+1:i+2+n_history]

        future_pred = history_stack
      
        #Compute metrics 
        if params.use_daily_climatology:
            clim = m[i:i+1]
            if params.interp > 0:
                clim_coarse = m_coarse[i:i+1]
        else:
            clim = m
            if params.interp > 0:
                clim_coarse = m_coarse

        pred = torch.unsqueeze(seq_pred[i], 0)
        tar = torch.unsqueeze(seq_real[i], 0)
        valid_loss[i] = weighted_rmse_torch_channels(pred, tar) * std
        acc[i] = weighted_acc_torch_channels(pred-clim, tar-clim)
        acc_unweighted[i] = unweighted_acc_torch_channels(pred-clim, tar-clim)

        if params.masked_acc:
          acc_land[i] = weighted_acc_masked_torch_channels(pred-clim, tar-clim, maskarray)
          acc_sea[i] = weighted_acc_masked_torch_channels(pred-clim, tar-clim, 1-maskarray)

        if params.interp > 0:
            pred = downsample(pred, scale=params.interp)
            tar = downsample(tar, scale=params.interp)
            valid_loss_coarse[i] = weighted_rmse_torch_channels(pred, tar) * std
            acc_coarse[i] = weighted_acc_torch_channels(pred-clim_coarse, tar-clim_coarse)
            acc_coarse_unweighted[i] = unweighted_acc_torch_channels(pred-clim_coarse, tar-clim_coarse)

        if params.log_to_screen:
          idx = idxes[fld] 
          logging.info('Predicted timestep {} of {}. {} RMS Error: {}, ACC: {}'.format(i, prediction_length, fld, valid_loss[i, idx], acc[i, idx]))
          if params.interp > 0:
            logging.info('[COARSE] Predicted timestep {} of {}. {} RMS Error: {}, ACC: {}'.format(i, prediction_length, fld, valid_loss_coarse[i, idx],
                        acc_coarse[i, idx]))

    seq_real = seq_real.cpu().numpy()
    seq_pred = seq_pred.cpu().numpy()
    valid_loss = valid_loss.cpu().numpy()
    acc = acc.cpu().numpy()
    acc_unweighted = acc_unweighted.cpu().numpy()
    acc_coarse = acc_coarse.cpu().numpy()
    acc_coarse_unweighted = acc_coarse_unweighted.cpu().numpy()
    valid_loss_coarse = valid_loss_coarse.cpu().numpy()
    acc_land = acc_land.cpu().numpy()
    acc_sea = acc_sea.cpu().numpy()

    return (np.expand_dims(seq_real[n_history:], 0), np.expand_dims(seq_pred[n_history:], 0), np.expand_dims(valid_loss,0), np.expand_dims(acc, 0),
           np.expand_dims(acc_unweighted, 0), np.expand_dims(valid_loss_coarse, 0), np.expand_dims(acc_coarse, 0),
           np.expand_dims(acc_coarse_unweighted, 0),
           np.expand_dims(acc_land, 0),
           np.expand_dims(acc_sea, 0))

-------------------------------------------------------------

    for i, ic in enumerate(ics):
      logging.info("Initial condition {} of {}".format(i+1, n_ics))
      sr, sp, vl, a, au, vc, ac, acu, accland, accsea = autoregressive_inference(params, ic, valid_data_full, model)

      if i ==0 or len(valid_loss) == 0:
        seq_real = sr
        seq_pred = sp
        valid_loss = vl
        valid_loss_coarse = vc
        acc = a
        acc_coarse = ac
        acc_coarse_unweighted = acu
        acc_unweighted = au
        acc_land = accland
        acc_sea = accsea
      else:
#        seq_real = np.concatenate((seq_real, sr), 0)
#        seq_pred = np.concatenate((seq_pred, sp), 0)
        valid_loss = np.concatenate((valid_loss, vl), 0)
        valid_loss_coarse = np.concatenate((valid_loss_coarse, vc), 0)
        acc = np.concatenate((acc, a), 0)
        acc_coarse = np.concatenate((acc_coarse, ac), 0)
        acc_coarse_unweighted = np.concatenate((acc_coarse_unweighted, acu), 0)
        acc_unweighted = np.concatenate((acc_unweighted, au), 0)
        acc_land = np.concatenate((acc_land, accland), 0)
        acc_sea = np.concatenate((acc_sea, accsea), 0)

