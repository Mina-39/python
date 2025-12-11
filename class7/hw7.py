num = int(
    input("請輸入一個數字: ")
)  # print請輸入一個數字:, 將輸入的字串轉換成整數, 存入num變數
if num < 2:  # 如果num小於2
    print("不是質數")
else:
    prime = True  # 假設是質數
    for i in range(2, num):  # 從2開始檢查到num-1
        if num % i == 0:  # 如果num能被i整除
            prime = False  # 就不是質數
            break  # 結束迴圈
    if prime:  # 如果prime仍然是True
        print("是質數")
    else:
        print("不是質數")
