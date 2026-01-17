def hello(name: str = "Singular") -> None:  # 函數傳入參數都是區域變數
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數:\n
    name" str - 姓名


    回傳:None

    範例:hello("Alice") # Hello, Alice!
    """
    print(f"Hello, {name}!")


# 讀取指令說明
print(hello.__doc__)


水果 = {"蘋果": 25, "香蕉": 20, "橘子": 30}


def edit():
    """修改水果價格"""
    新水果 = input("請輸入你要新增的水果名稱:")
    新價格 = input(f"請輸入{新水果}的價格")
    水果[新水果] = 新價格
    print(新水果, "以新增，價格", 新價格)


def add():
    """新增水果價格"""
    新水果 = input("請輸入你要修改的水果名稱:")
    新價格 = input(f"請輸入{新水果}的新價格")
    水果[新水果] = 新價格
    print(新水果, "以修改為", 新價格, "元")


def delete():
    """刪除水果"""
    新水果 = input("請輸入你要刪除的水果名稱:")
    del 水果[新水果]
    print(新水果, "以刪除")


功能清單 = [add, edit, delete]

while True:
    print("目前水果價格")
    for key in 水果:
        print(key, ":", 水果[key], "元")
    for i, 功能 in enumerate(功能清單, start=1):
        print(f"{i}. {功能.__doc__}")
    print(f"{len(功能清單)+1}. 離開系統")

    選擇 = int(input("請選擇功能(1~4): "))
    if 選擇 == (len(功能清單) + 1):
        print("感謝使用水果店價格查詢系統")
        break
    else:
        功能清單[選擇 - 1]()
    print("=" * 26)

# 適用__doc__屬性可以查看函式的說明文件
# 例如：
print(add.__doc__)
print(add.__name__)
# eval(input()) - 這個函式可以讓使用者輸入的文字變成程式碼來執行
# 例如：
ans = eval("3 + 5")
print(ans)  # 輸出8

# 這樣就可以讓使用者輸入數學運算式, 然後計算結果
# 例如：
ans = eval(input("請輸入數學運算式: "))
print(ans)
# 例如輸入：
# 5 + 3
# 輸出結果為8

# 檔案讀寫
# 判斷檔案是否存在 - 使用 os.path.isfile() 函式
import os

# 相對路徑代表相對於目前的工作目錄的路徑
# 絕對路徑代表完整的路徑
if os.path.isfile("class17/hw.py"):
    # C:\Users\User\Desktop\python_test\class17\hw.py
    print("檔案存在！")
else:
    print("檔案不存在！")

# open() 開啟模式
# r - 讀取模式、檔案必須存在
# w - 寫入模式、檔案不存在會自動建立
# a - 附加模式、檔案不存在會自動建立
# r+ - 讀取與寫入模式、檔案必須存在
# w+ - 讀取與寫入模式、檔案不存在會自動建立
# a+ - 讀取與附加模式、檔案不存在會自動建立

# 讀取檔案 - 使用 open() 函式
# 例如：
file = open("class18/file_test.py", "r")
print(file.read())
file.close()

# 讀取檔案 - 使用 with open() as
# 例如：
with open("class18/file_test.py", "r") as file:
    print(file.read())

# 寫入檔案 - 使用 open() 函式
# 例如：
file = open("class18/file_test.py", "w")
file.write("print('write file test')")
file.close()


# 寫入檔案 - 使用 with open() as
# 例如：
with open("class18/file_test.py", "w") as file:
    file.write("print('Hello World!')")
