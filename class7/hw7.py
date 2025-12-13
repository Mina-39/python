num = int(input("請輸入一個數字: "))
if num < 2:
    print("不是質數")
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("是質數")
    else:
        print("不是質數")
