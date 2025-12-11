import turtle as t

t.penup()
t.color("red")
t.shape("circle")
forw = 2
for i in range(108):
    t.forward(forw)
    t.stamp()
    t.right(10)
    forw += 0.5
t.done()
