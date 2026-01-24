# 附加檔案 - 使用open()函式
# 例如：
file = open("class18/file_test.py", "a")
file.write("\nprint('append file test')")
file.close()

# 附加檔案 - 使用with open() as
# 例如：
with open("class18/file_test.py", "a") as file:
    file.write("\nprint('append file test')")

# replace -  取代字串中的特定字串
# 例如：
text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  # 輸出 Hello, Python!

# strip - 移除字串開頭與結尾的空白
# 例如：
text = "   Hello, Python!   "
new_text = text.strip()
print(new_text)  # 輸出 Hello, Python!

# zfill - 字串補零
# 例如：
number = "a"
new_number = number.zfill(2)
print(new_number, type(new_number))  # 輸出 0a <class 'str'>

# datetime 模組
# datetime 模組可以處理日期與時間
import datetime

# 取得目前的日期與時間 - 使用 datetime.datetime.now() 函式
# 例如：
now = datetime.datetime.now()
print(now)  # 輸出目前的日期與時間

# 字串轉換成日期 - 使用 datetime.datetime.strptime() 函式
# 例如：
date = datetime.datetime.strptime("2024-06-01", "%Y-%m-%d")
print(date)  # 輸出 2024-06-01 00:00:00

# 有哪一些格式化字串可以使用？
# %Y - 年分(四位數)
# %m - 月份(兩位數)
# %d - 日期(兩位數)
# %H - 小時(24小時制, 兩位數)
# %M - 分鐘(兩位數)
# %S - 秒數(兩位數)
# 例如：
# %A - 星期幾(完整名稱)
# %B - 月份(完整名稱)
# %c - 日期和時間的字串表示
# %p - AM 或 PM
# 例如：
date = datetime.datetime.strptime("2024-01-01 12:30:45", "%Y-%m-%d %H:%M:%S")
print(date)  # 輸出 2024-01-01 12:30:45

# 日期轉換成字串 - 使用 datetime.datetime.strftime() 函式
# 例如：
date = datetime.datetime.now()

# 獲得一周天數
import datetime

now = datetime.datetime.now()
print(now.weekday())  # 輸出0~6, 0代表星期一, 6代表星期日

# Math 函數
math.fmod(x, y)  # 取餘數含小數點
math.fabs(x)  # 取絕對值
math.floor(x)  # 無條件捨去
math.ceil(x)  # 無條件進位
