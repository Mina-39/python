# for...else... 語法
# 當 for 迴圈正常執行完畢後會執行 else 區塊的程式
for i in range(5):
    print(i)
else:
    print("for 迴圈結束")
# while...else... 語法
# 當 while 迴圈正常執行完畢後會執行 else 區塊的程式
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while 迴圈結束")
# else 在python中有三種不同的用途
# 1. if...elif...else...: 當前面的條件都不成立時會執行 else 區塊的程式
# 2. try...except...else...: 當 try 區塊的程式沒有發生例外時會執行 else 區塊的程式
# 3. for...else... / while...else...: 當迴圈正常執行完畢後會執行 else 區塊的程式

# 迴圈的break可以用來跳出迴圈
# 所以判斷break屬於哪個迴圈時,要看它是在哪個迴圈內被執行
# 例如：
for i in range(5):
    for j in range(5):
        if j == 2 and i == 2:
            break  # 跳出內層迴圈
        print(f"i={i}, j={j}")
# 這裡的break是跳出內層的for j迴圈
# 外層的for i迴圈不受影響,會繼續執行

# 果汁飲料機範例
while True:
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 離開")
    choice = input("請選擇飲料(1-4):")
    if choice == "1":
        print("您選擇了蘋果汁")
    elif choice == "2":
        print("您選擇了柳橙汁")
    elif choice == "3":
        print("您選擇了葡萄汁")
    elif choice == "4":
        print("謝謝惠顧，再見！")
        break  # 跳出迴圈
    else:
        print("輸入錯誤查無此果汁，請重新選擇")

# 　continue
# 迴圈的continue可以用來跳過本回合的剩餘程式,直接進入下一回合, else可以正常執行
# 例如：
for i in range(5):
    if i == 2:
        continue  # 跳過本回合剩餘程式,直接進入下一回合
    print(i)
# 這裡的continue會跳過 i = 2 的那次迴圈, 直接進入下一回合
# 所以印出的結果會是0,1,3,4
# continue也可以用在while迴圈中
# 例如：
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue  # 跳過本回合剩餘程式,直接進入下一回合
    print(i)
# continue也要判斷屬於哪個迴圈
