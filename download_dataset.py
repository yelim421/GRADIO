typhoon_list = [
    {'id': '1825', 'dur': 49, 'start': '2018092800', 'end': '2018100712', 'latitude': 7.4, 'longitude': 150.9, 'lp': 900, 'hws': 115, 'grade': 5},
    # Add more typhoon data here...
]

data = '''
18092800 002 2 074 1509 1006     000                                            
18092806 002 2 085 1495 1004     000                                            
18092812 002 2 096 1480 1004     000                                            
18092818 002 2 110 1465 1002     000                                            
18092900 002 2 120 1442 1004     000                                            
18092906 002 3 126 1426 1000     035     00000 0000 90090 0090                  
18092912 002 3 128 1414  996     040     00000 0000 90120 0120                  
18092918 002 4 131 1399  990     050     00000 0000 90120 0120                  
18093000 002 4 137 1389  980     060     90040 0040 90150 0150                  
18093006 002 5 145 1381  975     065     90040 0040 90150 0150                  
18093012 002 5 149 1372  965     075     90060 0060 90180 0180                  
18093018 002 5 154 1364  950     085     90075 0075 90180 0180                  
18100100 002 5 156 1359  940     090     90090 0090 90210 0210                  
18100106 002 5 161 1352  925     100     90100 0100 90240 0240                  
18100112 002 5 168 1344  900     115     90120 0120 90240 0240                  
18100118 002 5 173 1336  900     115     90120 0120 90240 0240                  
18100200 002 5 177 1327  900     115     90120 0120 90240 0240                  
18100206 002 5 182 1320  900     115     90120 0120 90240 0240                  
18100212 002 5 189 1312  915     105     90120 0120 90350 0350                  
18100218 002 5 195 1304  940     090     90100 0100 90350 0350                  
18100300 002 5 201 1297  950     085     90100 0100 90350 0350                  
18100306 002 5 209 1292  955     080     90100 0100 90400 0400                  
18100312 002 5 216 1288  970     070     90100 0100 90400 0400                  
18100318 002 5 225 1281  975     065     90100 0100 90300 0300                  
18100400 002 5 232 1277  975     065     90120 0120 90300 0300                  
18100403 002 5 238 1274  975     065     90120 0120 90300 0300                  
18100406 002 4 243 1271  975     060     90120 0120 90300 0300                  
18100409 002 4 249 1269  975     060     90120 0120 90300 0300                  
18100412 002 4 254 1267  975     060     90100 0100 90300 0300                  
18100415 002 4 262 1264  975     060     90100 0100 90300 0300                  
18100418 002 4 267 1261  975     060     90100 0100 90300 0300                  
18100421 002 4 275 1259  975     060     90100 0100 90300 0300                  
18100500 002 4 280 1259  975     060     90100 0100 90300 0300                  
18100503 002 4 287 1259  975     060     90120 0120 90300 0300                  
18100506 002 5 295 1259  975     065     90140 0140 90300 0300                  
18100509 002 5 305 1261  975     065     90140 0140 90300 0300                  
18100512 002 5 313 1260  975     065     90140 0140 90300 0300                  
18100515 002 5 322 1261  975     065     90140 0140 90300 0300                  
18100518 002 5 329 1265  975     065     90140 0140 90300 0300                  
18100521 002 5 337 1273  975     065     90140 0140 90300 0300                  
18100600 002 4 347 1281  975     060     90120 0120 90300 0300                  
18100603 002 4 358 1291  980     055     90100 0100 90240 0240                  
18100606 002 4 371 1304  980     055     90100 0100 90240 0240                  
18100609 002 4 379 1317  980     055     90100 0100 90240 0240                  
18100612 002 6 389 1337  984     000                                            
18100618 002 6 410 1372  988     000                                            
18100700 002 6 420 1410  994     000                                            
18100706 002 6 423 1472  994     000                                            
18100712 002 6 412 1520  996     000
'''

lines = data.strip().split('\n')
formatted_data = ['20' + line.strip().replace(' ', '').ljust(8, '0') for line in lines]

# 결과 출력
for item in formatted_data:
    print(item)