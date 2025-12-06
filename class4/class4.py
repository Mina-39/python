import turtle as t  # 匯入模組turtle並取名為t

t.forword(100)  # 往前走100步
t.right(90)  # 往右轉90度
t.done()  # 結束,保持視窗打開

# 匯入方法統整
# 匯入整個模組
# import 模組名稱
# 使用模組內的方法時,需加上模組名稱.方法名稱
# from 模組名稱 import 方法名稱
# 直接使用方法名稱
# import 模組名稱 as 別名
# 使用模組內的方法時,需加上別名.方法名稱

import turtle as t

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.done()

# for example
# for的組成有三個部分, for in , 迴圈變數, 範圍
# for 迴圈變數 in 範圍:
# 迴圈變數只能活在for迴圈內
# 迴圈變數每回合都會從範圍中取出一個值
for i in range(5):  # range可以產生一組數字: 0,1,2,3,4
    print(i)

for i in range(1, 6):  # range(起始值, 終止值) 產生: 1,2,3,4,5
    print(i)

for i in range(1, 11, 2):  # range(起始值, 終止值, 步進值) 產生: 1,3,5,7,9
    print(i)


import turtle as t

for i in range(4):
    t.forward(100)
    t.right(90)
t.done()

# 蓋印章示範
import turtle as t

t.penup()  # 提起畫筆, 這樣就不會畫線但是可以移動
t.color("purple")  # 設定顏色為紫色
t.shape("turtle")  # 設定烏龜的形狀為烏龜
for i in range(120):
    t.forward(20)
    t.stamp()  # 蓋印章
    t.right(6)
t.done()
