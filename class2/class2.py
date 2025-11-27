# 運算子
print(1 + 2)  # 加法
print(5 - 3)  # 減法
print(4 * 2)  # 乘法
print(8 / 4)  # 除法
print(7 // 3)  # 取整數
print(7 % 3)  # 取餘數
print(2**3)  # 次方
# 優先順序
# 1. 括號 ()
# 2. 次方 **
# 3. + - 正負號
# 4. * / // % 乘 除 取整數 取餘數
# 5. + - 加 減
print(3 + 4 * 2)  # 11
print((3 + 4) * 2)  # 14
print(2**3**2)  # 512，次方是由右往左算
# 字串運算
print("Hello " + "World")  # 字串串接
print("Hi " * 3)  # 字串重複
# 認識基本指令
# 指令會有名稱跟括號組成，括號內可以放材料(參數)
# 每個材料之間要用逗號分隔
ma = max(3, 5, 2, 8, 1)  # 取最大值
print(ma)
l = len("Hello World")  # 取長度
print(l)
# type() 可以查看材料的型態
print(type(123))  # 取型態
print(type("Hello"))  # 取型態
print(type(12.34))  # 取型態
print(type(True))  # 取型態
# 型態轉換
# str() 轉成字串
# int() 轉成整數
# float() 轉成浮點數
# bool() 轉成布林值
print(int("123"))  # => 123
print(int(12.34))  # => 12
print(int(True))  # => 1
print(int(False))  # => 0
print("-----------------------")
print(float("12.34"))  # => 12.34
print(float(123))  # => 123.0
print(float(True))  # => 1.0
print(float(False))  # => 0.0
print("-----------------------")
print(str(123))  # => "123"
print(str(12.34))  # => "12.34"
print(str(True))  # => "True"
print(str(False))  # => "False"
print("-----------------------")
print(bool(1))  # => True
print(bool(0))  # => False
print(bool(12.34))  # => True
print(bool(0.0))  # => False
print(bool("Hello"))  # => True

# input() 可以讓使用者在終端機中輸入資料
print("開始輸入資料：")
input()
print("結束輸入資料")
# input() 的括弧內可以放提示使用者輸入的字串
name = input("請輸入你的名字：")
print("你的名字是：" + name)
print("Hello " + name)  # 字串相加
# 正方形面積計算
s = input("請輸入正方形邊長：")
s = int(s)  # 轉換成整數
area = s * s  # 面積計算
print(f"正方形面積是：{area}")  # 印出結果(面積)
