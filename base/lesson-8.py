# Псевдослучайные числа
from random import *

print(randint(1, 100))  # целое число от а до b
print(uniform(1, 100))  # дробное число от a до b
print(random())  # дробное число от 0 до 1

data = ["Vova", "Boris", "Julia"]
print(choice(data))
print(choices(data, k=2))
print(sample(data, k=2))  # уникальные элементы
shuffle(data)
print(data)

x1, y1 = 0, 1
x2 = y2 = 0
