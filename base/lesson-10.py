# Цикл while

# Нахождение суммы цифр числа любой длины

num = 123
summ = 0
while num > 0:
    summ += num % 10
    num //= 10
print(summ)

# Цикл for

# range(n, m , k) - создает числовой диапозон от n до m с шагом k
print(*range(1,13)) # от 5 до 13 не включительно
print(*range(10)) # от 0 до 10 не включительно
print(*range(4,10,2)) # от 4 до 10 не включительно с шагом 2

for i in range(0,-13, -3):
    print(i)

data = [ "user1", "user2", "user3"]
for i in data:
    print(i)


#################################################################
# Напишите программу, которая выводит на экран количество разрядов введенного пользователем числа
num = int(input())
def count_of_number(num):
    num2 = 0
    while num > 0:
        num //= 10
        num2 +=1
    return num2
print(count_of_number(547))