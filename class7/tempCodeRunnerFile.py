while True:
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 離開")
    choice = input("請選擇飲料(1-4):")
    if choice == "1":
        print("您選擇了蘋果汁")
    elif choice == "2":
        print("您選擇了柳橙汁")
    elif choice == "3":
        print("您選擇了葡萄汁")
    elif choice == "4":
        print("謝謝惠顧，再見！")
        break  # 跳出迴圈
    else:
        print("輸入錯誤查無此果汁，請重新選擇")