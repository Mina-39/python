import random  # 這是隨機模組, 也可以重新取名為其他名稱, 例如: import random as rnd

# random.randrange 設定範圍的方式與range()一樣，特性也一樣不包含終止值(最後一個數字)
# random.randrange 的功能是從指定範圍內隨機選取一個整數, range是產生一組數字
print(random.randrange(10))  # 從0~9隨機選取一個整數
print(random.randrange(1, 10))  # 從1~9隨機選取一個整數
print(random.randrange(1, 10, 2))  # 從[1,3,5,7,9]隨機選取一個整數

# random.randint 的功能是從指定範圍內隨機選取一個整數, 包含終止值(最後一個數字)
# 不能跳數字抽籤
print(random.randint(1, 10))  # 從1~10隨機選取一個整數

# CRUD 介紹
# CRUD 是 Create, Read, Update, Delete 的縮寫
# Create: 建立資料
# Read: 讀取資料
# Update: 更新資料
# Delete: 刪除資料

# List 清單 (List)
# List 可以存入很多資料，每筆資料用`，`隔開
# List 可以存入不同型態的資料
# List 最外層用`[]`包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "Hello", ["World", 6]]  # 數字, 字串, List
print(L)

# List 取值
# List 取值的方式跟字串一樣, 用'[]'取值
L = [1, 2, 3, 4, 5]
print(L[0])  # 取第一個值
print(L[1])  # 取第二個值
print(L[2])  # 取第三個值

# List 取值的方式跟字串一樣, 也可以用'[:]'取值
# 設定範圍的方式跟range很像, 不包含終止值(最後一個數字)
print(L[1:4:2])  # 取出第二個到第四個值, 步進值(間隔)為2, 結果為[2,4]
print(L[0:3])  # 取出第一個到第三個值, 結果為[1,2,3]
print(L[:3])  # 取出第一個到第三個值, 結果為[1,2,3]
print(L[:])  # 取出所有值, 結果為[1,2,3,4,5]

# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得List長度, 也就是List當中有幾筆資料

# 不要跟index混淆, index是資料的編號, len是資料的數量
for i in range(len(L)):
    print(L[i])

for i in L:
    print(i)
# 要使用哪一種方式取得List當中的資料, 要看使用的環境中會不會需要用到index編號

juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]

while True:
    for index in range(len(juice_list)):
        print(f"{index + 1}. {juice_list[index]}")
    choice = int(input("請輸入編號: "))
    if choice < 1 or choice > len(juice_list):
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    if choice == len(juice_list):
        print("謝謝惠顧，再見！")
        break
    print(f"您選擇了{juice_list[choice - 1]}")

# List 更新資料
# 用起來跟一般的變數很像
# 要注意的是記得指定index(編號)位置
L = ["Apple", "Banana", "Cherry"]
L[1] = "Orange"  # 將索引1的資料改成Orange
# call by value
# 在一般情況下, 存資料到變數當中是採用call by value的方式
a = 1
b = a
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置, 所以改變b的值, a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b, 但是b跟a指向不同的記憶體位置
b[0] = 2
print(a, b)
