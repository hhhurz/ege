# Способы найти сумму цифр числа в любой системе счисления

from string import printable as alph

data = '312231'

sum_1 = sum(map(int, data))
sum_2 = sum(map(lambda x: int(x, 36), data))
sum_3 = data.count('1') + data.count('2') * 2 + data.count('3') * 3
sum_4 = 0
for i in range(37):
    sum_4 += data.count(alph[i]) * i
sum_5 = 0
for i in set(data):
    sum_5 += data.count(i) * int(i, 36)

# Вариации списочных включений, аналог sum_4 и sum_5
sum_6 = sum([data.count(alph[i]) * i for i in range(37)])
sum_7 = sum([data.count(i) * int(i, 36) for i in set(data)])
sum_8 = sum(data.count(alph[i]) * i for i in range(37))


