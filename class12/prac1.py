print("=== 水果店價格查詢系統 ===")

# 水果資料（Dictionary）
d = {"蘋果": 25, "香蕉": 20, "橘子": 30}


# 顯示水果價格（直的）
def show_prices():
    print("\n目前水果價格：")
    for fruit, price in d.items():
        print(f"{fruit}: {price}元")


# 主程式
while True:
    show_prices()
    print("\n1. 新增水果價格")
    print("2. 修改水果價格")
    print("3. 刪除水果")
    print("4. 離開系統")

    choice = input("請選擇功能 (1-4)：")
    print("==========================")

    # 新增水果
    if choice == "1":
        fruit = input("請輸入要新增的水果名稱：")
        price = int(input(f"請輸入{fruit}的價格："))

        if fruit in d:
            print("水果已存在")
        else:
            d[fruit] = price
            print(f"{fruit}已新增，價格為{price}元")
            print("==========================")
    # 修改水果價格
    elif choice == "2":
        fruit = input("請輸入要修改的水果名稱：")
        if fruit in d:
            price = int(input("請輸入新的價格："))
            d[fruit] = price
            print(f"{fruit}價格已修改為{price}元")
            print("==========================")
        else:
            print("找不到此水果")

    # 刪除水果（使用 pop）
    elif choice == "3":
        fruit = input("請輸入要刪除的水果名稱：")
        result = d.pop(fruit, "不存在這筆資料")
        print(f"{fruit}已刪除")
        print("==========================")
    # 離開系統
    elif choice == "4":
        print("感謝使用水果店價格查詢系統！")
        break

    else:
        print("請輸入 1～4 的數字")
