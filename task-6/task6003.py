from turtle import *


screensize(10000, 10000)
lt(90)
tracer(0)
m = 10
for i in range(3,7,3):
    fd(10*10)
    rt(90)
    fd(20*10)
    rt(90)
up()
fd(3*m)
rt(90)
fd(7*m)
lt(90)
down()
for i in range(2):
    fd(70*m)
    rt(90)
    fd(90*m)
    rt(90)

for x in range(7,21):
    for y in range(3,11):
        teleport(x*m,y*m)
        dot(3,'red')
print(14*8)


update()
done()