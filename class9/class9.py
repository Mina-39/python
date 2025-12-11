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
