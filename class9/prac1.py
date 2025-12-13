weather = [
    "晴天",
    "多雲",
    "雨天",
    "晴天",
    "多雲",
    "雷陣雨",
    "晴天",
]  # 將"晴天"...存入變數weather裡面
print(weather)
while True:
    day = input("請輸入要修改的星期數字(1~7): ")
    try:
        day = int(day)  # 將day轉為整數型態
    except:
        print("請輸入數字, 不然自己重新學數學: ")  # 如果轉型態失敗
        continue  # 繼續
    if day < 1 or day > 7:
        print("輸入錯誤查無此日期，請重新輸入: ")
        continue
    new_weather = input(
        "請輸入新的天氣狀況: "
    )  # 將使用者輸入的新天氣存入變數new_weather
    weather[day - 1] = new_weather  # [day - 1]是將編號-1
    print(f"修改後的天氣狀況: {weather}")
    break  # 結束while迴圈
