shopping_list = []


def show_list():
    print("\n📋 目前購物清單：")
    if not shopping_list:
        print("（清單是空的）")
    else:
        for i, item in enumerate(shopping_list):
            print(f"{i}. {item}")


while True:
    show_list()
    print("\n請選擇功能：")
    print("1. 新增東西")
    print("2. 修改東西")
    print("3. 刪除東西")
    print("4. 離開程式")

    choice = input("請輸入 1~4：")

    # 新增
    if choice == "1":
        print("\na. 新增到最後面")
        print("b. 新增到指定位置")
        sub = input("請輸入 a 或 b：")

        if sub == "a":
            item = input("要新增什麼？")
            shopping_list.append(item)

        elif sub == "b":
            item = input("要新增什麼？")
            pos = int(input("要插入的位置（數字）："))
            shopping_list.insert(pos, item)

    # 修改
    elif choice == "2":
        print("\na. 用編號修改")
        print("b. 用名稱修改")
        sub = input("請輸入 a 或 b：")

        if sub == "a":
            pos = int(input("要修改的編號："))
            new_item = input("新的內容：")
            shopping_list[pos] = new_item

        elif sub == "b":
            old = input("要修改的名稱：")
            if old in shopping_list:
                new_item = input("新的內容：")
                index = shopping_list.index(old)
                shopping_list[index] = new_item
            else:
                print("清單裡沒有這個東西")

    # 刪除
    elif choice == "3":
        print("\na. 用名稱刪除")
        print("b. 用位置刪除")
        sub = input("請輸入 a 或 b：")

        if sub == "a":
            item = input("要刪除的名稱：")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("清單裡沒有這個東西")

        elif sub == "b":
            pos = int(input("要刪除的編號："))
            shopping_list.pop(pos)

    # 離開
    elif choice == "4":
        print("👋 不想逛了就回家吧！")
        break

    else:
        print("請輸入正確的選項")
