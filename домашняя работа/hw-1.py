from turtle import *

tracer(0)
screensize(10000000,10000000)
lt(90)
m = 10
for i in range(6):
     fd(33*m)
     rt(90)
     fd(20*m)
     rt(90)
up()
fd(3*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(6):
    fd(24*m)
    rt(90)
    fd(25*m)
    rt(90)
for x in range(9,21):
    for y in range(3,28):
        teleport(x*m,y*m)
        dot(3,"red")

print(10*23)




update()
done()