import turtle as t

t.penup()  # 提起畫筆, 這樣就不會畫線但是可以移動
t.color("purple")  # 設定顏色為紫色
t.shape("turtle")  # 設定烏龜的形狀為烏龜
for i in range(120):
    t.forward(20)
    t.stamp()  # 蓋印章
    t.right(6)
t.done()