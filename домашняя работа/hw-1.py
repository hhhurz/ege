from turtle import *
lt(90)
tracer(0)
m = 10
screensize(10000000,10000000)

for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)
for x in range(-10,10):
    for y in range(-10,10):
        teleport(x*m,y*m)
        dot(3,"red")
update()
done()

