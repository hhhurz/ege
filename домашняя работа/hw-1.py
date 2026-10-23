from turtle import *

screensize(100000,100000)
m=10
tracer(0)
lt(90)
for i in range(2):
    fd(25*m)
    rt(90)
    fd(10*m)
    rt(90)
fd(3*m)
lt(90)
fd(15*m)
rt(90)
for i in range(2):
    fd(9*m)
    rt(90)
    fd(32*m)
    rt(90)
for x in range(-10,10):
    for y in range(-10,10):
        teleport(x*m,y*m)
        dot(3,"red")
print(250,9*32)

update()
done()

