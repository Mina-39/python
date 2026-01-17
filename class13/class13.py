# def
# 新增一個函數要用 def 開頭, 後面接函數名稱和括號, 最後以冒號結尾
def hello():
    print("Hello, world!")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數 name, 當呼叫這個函數時, 可以傳入一筆資料給 name
def hello(name):
    print(f"Hello, {name}!")


hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello(i)


# 有回傳值的函數
# 這個函數會回傳一個值, 當呼叫這個函數時, 可以取得回傳的值
def add(a, b):
    return a + b


print(add(1, 2))
print(add("Hello, ", "world!"))
sum = add(3, 4)  # 可以將回傳值存到變數中
print(sum)


# 多個回傳值的函數
# 這個函數會回傳兩個值, 當呼叫這個函數時, 可以把回傳的值存起來
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 將回傳的兩個值分別存到 sum 和 sub 變數中
print(f"sum: {sum}, sub: {sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))  # 結果為 -1
print(add_sub(5, 6))  # 結果為 11


# 預設參數
# 可以在函數的參數中設定預設值, 當呼叫函數時, 如果沒有傳入該參數的值, 就會使用預設值
def hello(name, message="Hello"):
    print(f"{message}, {name}!")


# 如果是 def hello(message="Hello", name): 會發生錯誤, 因為預設參數必須放在非預設參數的後面
hello("Alice")
hello("Bob", "Good morning")
# 使用指令時指定參數
hello(name="Charlie", message="Hi")
hello(message="Good Evening", name="David")
# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    # length = length + 1 # 這行會出錯，
    # 因為在函數內部length是區域變數，不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是", area) # 這行會出錯，因為area是區域變數，只能在函數內部使用

length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area()  # 面積是 100
# 因為要等到函數被呼叫時才會執行，所以area的值是在函數被呼叫時才會被計算

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 100
# 這時候指令內部的area是區域變數，不會影響到全域變數的值

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area() -> int:
    area = length**2  # length是全域變數, area是區域變數
    return area


area = calculate_square_area()
print("面積是", area)  # 面積是 25

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    global area  # 使用global，將area變成全域變數
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 25
