try:
    ftemp = float(input("請輸入華氏溫度:"))
    ctemp = (ftemp - 32) * 5 / 9
    print(f"華氏溫度: {ftemp}F等於攝氏溫度: {ctemp}C")
except:
    print("輸入錯誤！請輸入數字")
