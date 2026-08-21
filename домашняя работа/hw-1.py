# Задание 1
num = int(input())
if num % 10 == 0 or num % 10 == 5 or num % 10 == 2:
    print(num)
else:
    print(num + 1)

# Задание 2
num = int(input())
if num > 0:
    print(num + 1)
else:
    print(num - 1)

# Задание 3
num = int(input())
if 0 < num < 100:
    if num % 3 == 0:
        print(num // 3)
    else:
        print(num * 2)

# Задание 4
x = int(input())
if x > 0:
    print(x * 2 + 5)
elif x < 0:
    print( x ** 2 - 1)
else:
    print(x)

# Задание 5
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x2-x1) == 2 and abs(y2-y1) == 1 or abs(x2-x1) == 1 and abs(y2-y1) == 2 :
    print("Yes")
else:
    print("No")
