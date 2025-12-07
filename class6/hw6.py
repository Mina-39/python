total = 0
while True:
    money = int(input("請輸入商品金額: "))
    if money == 0:
        break
    total += money
    print(f"總金額為: {total} 元")
