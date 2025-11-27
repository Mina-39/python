# try expect
# 錯誤處理
try:
    # 可能會發生錯誤的程式碼
    num = int(input("請輸入一個整數: "))
except:
    # 發生錯誤時要執行的程式碼
    print("輸入的不是整數，請重新輸入。")
else:
    # 沒有發生錯誤時要執行的程式碼
    print(num + 100000)
# 以作業為例：
try:
    h = float(input("請輸入身高: "))
    w = float(input("請輸入體重: "))
    bmi = w / h**2
    print(f"你的 BMI 是: {bmi}")
except:
    print("輸入的身高或體重不是數字，請重新輸入")

# 比較運算子
print(1 == 1)  # True, 1 == 1
print(1 != 1)  # False, 1 != 1
print(1 > 0)  # True, 1 > 0
print(1 < 0)  # False, 1 < 0
print(1 >= 1)  # True, 1 >= 1
print(1 <= 0)  # False, 1 <= 0
# 邏輯運算子
# and 全部都成立或符合標準才會回傳 True
# or 有一個成立或符合標準就會回傳 True
# not 取原布林值的相反

print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(not True)  # False, 不是True
print(not False)  # True, 不是False

# 優先順序
# 1. 括號 ()
# 2. 次方 **
# 3. + - 正負號
# 4. * / // % 乘 除 取整數 取餘數
# 5. + - 加 減
# 6. == != > < >= <= 比較運算子
# 7. not 邏輯運算子
# 8. and 邏輯運算子
# 9. or 邏輯運算子

# if 條件判斷
password = input("請輸入密碼: ")
if password == "123456":  # 若密碼為 123456
    print("登入成功")

# if else
password = input("請輸入密碼: ")
if password == "123456":  # 若密碼為 123456
    print("登入成功")
else:
    print("密碼錯誤")

# if elif else
password = input("請輸入密碼: ")
if password == "123456":  # 若密碼為 123456
    print("登入成功")
elif password == "000000":
    print("密碼為預設密碼，請修改密碼")
else:
    print("密碼錯誤")

# if elif else是連續的判斷，只要有一個條件符合，就不會繼續往下判斷
# if 只能一個一定要有，elif 可以有多個且可有可無，else 只能一個且可有可無
