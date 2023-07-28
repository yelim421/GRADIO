from PIL import Image
def warning_message(typhoon, area, dates, time):
    if dates == "October 5th, 2018":
        if area == "Seoul":
            if time == "00:00":
                image_path = "sample_18100500.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100506.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100512.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100518.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다."

        elif area == "Gangwon Province (Gangneung)":
            if time == "00:00":
                image_path = "sample_18100500.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 43.9mm 정도의 비가 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100506.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 43.9mm 정도의 비가 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100512.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 43.9mm 정도의 비가 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100518.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 43.9mm 정도의 비가 예상됩니다."

        elif area == "Gyeongsang Province (Yeongdeok)":
            if time == "00:00":
                image_path = "sample_18100500.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 83.5mm 정도의 비가 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100506.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 83.5mm 정도의 비가 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100512.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 83.5mm 정도의 비가 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100518.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 83.5m 정도의 비가 예상됩니다."

        elif area == "Busan":
            if time == "00:00":
                image_path = "sample_18100500.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 51.3mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "06:00":
                image_path = "sample_18100506.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 51.3mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "12:00":
                image_path = "sample_18100512.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 51.3mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "18:00":
                image_path = "sample_18100518.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 51.3mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."


        elif area == "Southern Region (Namhae)":
            if time == "00:00":
                image_path = "sample_18100500.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "06:00":
                image_path = "sample_18100506.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "12:00":
                image_path = "sample_18100512.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "18:00":
                image_path = "sample_18100518.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."

        elif area == "Jeolla Province (Gwangju)":
            if time == "00:00":
                image_path = "sample_18100500.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "06:00":
                image_path = "sample_18100506.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "12:00":
                image_path = "sample_18100512.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."
            elif time == "18:00":
                image_path = "sample_18100518.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 36.5mm 정도의 비가 예상됩니다.\n해안 지역은 너울성 파도가 도로 및 방파제를 넘어설 것으로 예상되므로 주의가 필요합니다.\n항해 및 조업 시, 파도 상태를 확인하고 안전 대비책을 마련하시길 바랍니다."

        elif area == "Jeju Island":
            if time == "00:00":
                image_path = "sample_18100500.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 63.3mm 정도의 비가 예상됩니다.\n일 강수량 310.0mm 정도의 많은 비가 내릴 것으로 예상되므로, 지역적인 홍수 및 저지대 침수에 주의하시길 바랍니다.\n산사태 위험이 있으니 인근 주민은 가까운 대피소로 대피하시길 권장합니다.\n차량 및 농작물시설 파손에 유의하세요.\n저희의 예측에 따르면, 10월 역대 최다 강수량 갱신할 것으로 보입니다."
            elif time == "06:00":
                image_path = "sample_18100506.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 63.3mm 정도의 비가 예상됩니다.\n일 강수량 310.0mm 정도의 많은 비가 내릴 것으로 예상되므로, 지역적인 홍수 및 저지대 침수에 주의하시길 바랍니다.\n산사태 위험이 있으니 인근 주민은 가까운 대피소로 대피하시길 권장합니다.\n차량 및 농작물시설 파손에 유의하세요.\n저희의 예측에 따르면, 10월 역대 최다 강수량 갱신할 것으로 보입니다."
            elif time == "12:00":
                image_path = "sample_18100512.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 63.3mm 정도의 비가 예상됩니다.\n일 강수량 310.0mm 정도의 많은 비가 내릴 것으로 예상되므로, 지역적인 홍수 및 저지대 침수에 주의하시길 바랍니다.\n산사태 위험이 있으니 인근 주민은 가까운 대피소로 대피하시길 권장합니다.\n차량 및 농작물시설 파손에 유의하세요.\n저희의 예측에 따르면, 10월 역대 최다 강수량 갱신할 것으로 보입니다."
            elif time == "18:00":
                image_path = "sample_18100518.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 63.3mm 정도의 비가 예상됩니다.\n일 강수량 310.0mm 정도의 많은 비가 내릴 것으로 예상되므로, 지역적인 홍수 및 저지대 침수에 주의하시길 바랍니다.\n산사태 위험이 있으니 인근 주민은 가까운 대피소로 대피하시길 권장합니다.\n차량 및 농작물시설 파손에 유의하세요.\n저희의 예측에 따르면, 10월 역대 최다 강수량 갱신할 것으로 보입니다."

    if dates == "October 6th, 2018":
        if area == "Seoul":
            if time == "00:00":
                image_path = "sample_18100600.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 55.5mm 정도의 비가 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100606.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 55.5mm 정도의 비가 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100612.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 55.5mm 정도의 비가 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100618.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 55.5mm 정도의 비가 예상됩니다."

        elif area == "Gangwon Province (Gangneung)":
            if time == "00:00":
                image_path = "sample_18100600.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 135.3mm 정도의 많은 비와 20~30m/s의 강풍이 예상됩니다.\n따라서 도로 및 주택이 침수될 위험이 보이므로 위험 지역주민은 대피하시길 권장합니다.\n산사태로 인한 토사물 주의가 필요하며 간판 및 가로수를 조심하시길 바랍니다."
            elif time == "06:00":
                image_path = "sample_18100606.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 135.3mm 정도의 많은 비와 20~30m/s의 강풍이 예상됩니다.\n따라서 도로 및 주택이 침수될 위험이 보이므로 위험 지역주민은 대피하시길 권장합니다.\n산사태로 인한 토사물 주의가 필요하며 간판 및 가로수를 조심하시길 바랍니다."
            elif time == "12:00":
                image_path = "sample_18100612.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 135.3mm 정도의 많은 비와 20~30m/s의 강풍이 예상됩니다.\n따라서 도로 및 주택이 침수될 위험이 보이므로 위험 지역주민은 대피하시길 권장합니다.\n산사태로 인한 토사물 주의가 필요하며 간판 및 가로수를 조심하시길 바랍니다."
            elif time == "18:00":
                image_path = "sample_18100618.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 135.3mm 정도의 많은 비와 20~30m/s의 강풍이 예상됩니다.\n따라서 도로 및 주택이 침수될 위험이 보이므로 위험 지역주민은 대피하시길 권장합니다.\n산사태로 인한 토사물 주의가 필요하며 간판 및 가로수를 조심하시길 바랍니다."

        elif area == "Gyeongsang Province (Yeongdeok)":
            if time == "00:00":
                image_path = "sample_18100600.png"
                alert = f"Today is {dates}, and you are in {area}.\n낮 12시 이후 경상북도는 태풍의 영향권으로 진입할 가능성이 있으므로 주의가 필요합니다.\n경상북도는 300mm 정도의 폭우가 예상되므로 저지대 침수 및 지역적 홍수에 주의하시길 바랍니다.\n선박 및 어선은 미리 대피하기를 권장합니다."
            elif time == "06:00":
                image_path = "sample_18100606.png"
                alert = f"Today is {dates}, and you are in {area}.\n낮 12시 이후 경상북도는 태풍의 영향권으로 진입할 가능성이 있으므로 주의가 필요합니다.\n경상북도는 300mm 정도의 폭우가 예상되므로 저지대 침수 및 지역적 홍수에 주의하시길 바랍니다.\n선박 및 어선은 미리 대피하기를 권장합니다."
            elif time == "12:00":
                image_path = "sample_18100612.png"
                alert = f"Today is {dates}, and you are in {area}.\n낮 12시 이후 경상북도는 태풍의 영향권으로 진입할 가능성이 있으므로 주의가 필요합니다.\n경상북도는 300mm 정도의 폭우가 예상되므로 저지대 침수 및 지역적 홍수에 주의하시길 바랍니다.\n선박 및 어선은 미리 대피하기를 권장합니다."
            elif time == "18:00":
                image_path = "sample_18100618.png"
                alert = f"Today is {dates}, and you are in {area}.\n낮 12시 이후 경상북도는 태풍의 영향권으로 진입할 가능성이 있으므로 주의가 필요합니다.\n경상북도는 300mm 정도의 폭우가 예상되므로 저지대 침수 및 지역적 홍수에 주의하시길 바랍니다.\n선박 및 어선은 미리 대피하기를 권장합니다."

        elif area == "Busan":
            if time == "00:00":
                image_path = "sample_18100600.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 67.4mm 정도의 비와 33.6m/s 의 강풍이 예상됩니다.\n해안도로 및 인근 건물은 폭풍 해일에 주의하시길 바랍니다.\n사람이 날아갈 정도의 강한 바람이 불 것으로 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100606.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 67.4mm 정도의 비와 33.6m/s 의 강풍이 예상됩니다.\n해안도로 및 인근 건물은 폭풍 해일에 주의하시길 바랍니다.\n사람이 날아갈 정도의 강한 바람이 불 것으로 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100612.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 67.4mm 정도의 비와 33.6m/s 의 강풍이 예상됩니다.\n해안도로 및 인근 건물은 폭풍 해일에 주의하시길 바랍니다.\n사람이 날아갈 정도의 강한 바람이 불 것으로 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100618.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 67.4mm 정도의 비와 33.6m/s 의 강풍이 예상됩니다.\n해안도로 및 인근 건물은 폭풍 해일에 주의하시길 바랍니다.\n사람이 날아갈 정도의 강한 바람이 불 것으로 예상됩니다."


        elif area == "Southern Region (Namhae)":
            if time == "00:00":
                image_path = "sample_18100600.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n일 강수량 225.0mm 정도의 폭우가 예상됩니다.\n지역적 홍수 및 건물 침수에 주의하시길 바랍니다.\n10m이상의 높은 파도가 예상되므로 어선 및 선박은 미리 대피하는 것을 권장합니다. "
            elif time == "06:00":
                image_path = "sample_18100606.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n일 강수량 225.0mm 정도의 폭우가 예상됩니다.\n지역적 홍수 및 건물 침수에 주의하시길 바랍니다.\n10m이상의 높은 파도가 예상되므로 어선 및 선박은 미리 대피하는 것을 권장합니다. "
            elif time == "12:00":
                image_path = "sample_18100612.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n일 강수량 225.0mm 정도의 폭우가 예상됩니다.\n지역적 홍수 및 건물 침수에 주의하시길 바랍니다.\n10m이상의 높은 파도가 예상되므로 어선 및 선박은 미리 대피하는 것을 권장합니다. "
            elif time == "18:00":
                image_path = "sample_18100618.png"
                alert = f"Today is {dates}, and you are in {area}.\n일 강수량 80.0mm 정도의 비가 예상됩니다.\n일 강수량 225.0mm 정도의 폭우가 예상됩니다.\n지역적 홍수 및 건물 침수에 주의하시길 바랍니다.\n10m이상의 높은 파도가 예상되므로 어선 및 선박은 미리 대피하는 것을 권장합니다. "

        elif area == "Jeolla Province (Gwangju)":
            if time == "00:00":
                image_path = "sample_18100600.png"
                alert = f"Today is {dates}, and you are in {area}.\n금일 태풍 상륙으로, 높은 파고가 예상되므로 어선 대피와 항로와 여객선 전면 통제하는 것을 권장합니다.\n농작물 및 농업시설물 피해에 주의하시길 바랍니다."
            elif time == "06:00":
                image_path = "sample_18100606.png"
                alert = f"Today is {dates}, and you are in {area}.\n금일 태풍 상륙으로, 높은 파고가 예상되므로 어선 대피와 항로와 여객선 전면 통제하는 것을 권장합니다.\n농작물 및 농업시설물 피해에 주의하시길 바랍니다."
            elif time == "12:00":
                image_path = "sample_18100612.png"
                alert = f"Today is {dates}, and you are in {area}.\n금일 태풍 상륙으로, 높은 파고가 예상되므로 어선 대피와 항로와 여객선 전면 통제하는 것을 권장합니다.\n농작물 및 농업시설물 피해에 주의하시길 바랍니다."
            elif time == "18:00":
                image_path = "sample_18100618.png"
                alert = f"Today is {dates}, and you are in {area}.\n금일 태풍 상륙으로, 높은 파고가 예상되므로 어선 대피와 항로와 여객선 전면 통제하는 것을 권장합니다.\n농작물 및 농업시설물 피해에 주의하시길 바랍니다."

        elif area == "Jeju Island":
            if time == "00:00":
                image_path = "sample_18100600.png"
                alert = f"Today is {dates}, and you are in {area}.\n전날의 많은 강수량으로 인한 저수지 및 하천 범람에 주의하시길 바랍니다.\n금일 태풍 상륙으로 33m/s 정도의 강풍이 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100606.png"
                alert = f"Today is {dates}, and you are in {area}.\n전날의 많은 강수량으로 인한 저수지 및 하천 범람에 주의하시길 바랍니다.\n금일 태풍 상륙으로 33m/s 정도의 강풍이 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100612.png"
                alert = f"Today is {dates}, and you are in {area}.\n전날의 많은 강수량으로 인한 저수지 및 하천 범람에 주의하시길 바랍니다.\n금일 태풍 상륙으로 33m/s 정도의 강풍이 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100618.png"
                alert = f"Today is {dates}, and you are in {area}.\n전날의 많은 강수량으로 인한 저수지 및 하천 범람에 주의하시길 바랍니다.\n금일 태풍 상륙으로 33m/s 정도의 강풍이 예상됩니다."

    if dates == "October 7th, 2018":
        if area == "Seoul":
            if time == "00:00":
                image_path = "sample_18100700.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100706.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100712.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100718.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."

        elif area == "Gangwon Province (Gangneung)":
            if time == "00:00":
                image_path = "sample_18100700.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100706.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100712.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100718.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."

        elif area == "Gyeongsang Province (Yeongdeok)":
            if time == "00:00":
                image_path = "sample_18100700.png"
                alert = f"Today is {dates}, and you are in {area}.\n전일 산사태로 인한 토사물 주의하시길 바랍니다."
            elif time == "06:00":
                image_path = "sample_18100706.png"
                alert = f"Today is {dates}, and you are in {area}.\n전일 산사태로 인한 토사물 주의하시길 바랍니다."
            elif time == "12:00":
                image_path = "sample_18100712.png"
                alert = f"Today is {dates}, and you are in {area}.\n전일 산사태로 인한 토사물 주의하시길 바랍니다."
            elif time == "18:00":
                image_path = "sample_18100718.png"
                alert = f"Today is {dates}, and you are in {area}.\n전일 산사태로 인한 토사물 주의하시길 바랍니다."

        elif area == "Busan":
            if time == "00:00":
                image_path = "sample_18100700.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100706.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100712.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100718.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."


        elif area == "Southern Region (Namhae)":
            if time == "00:00":
                image_path = "sample_18100700.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100706.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100712.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100718.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."

        elif area == "Jeolla Province (Gwangju)":
            if time == "00:00":
                image_path = "sample_18100700.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100706.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100712.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100718.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."

        elif area == "Jeju Island":
            if time == "00:00":
                image_path = "sample_18100700.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "06:00":
                image_path = "sample_18100706.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "12:00":
                image_path = "sample_18100712.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
            elif time == "18:00":
                image_path = "sample_18100718.png"
                alert = f"Today is {dates}, and you are in {area}.\n강수가 없을것으로 예상됩니다."
    return alert, image_path