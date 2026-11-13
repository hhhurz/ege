# from string import printable as alph
# def convert(num,sys):
#     res = ""
#     while num:
#         res += str(num % sys)
#         num //= sys
#     return res[::-1] if res else "0"
#
#
#
# ans = []
# for n in range(1,100000):
#     r = convert(n,3)
#     if (r.count("1") + r.count("2") * 2  ) % 3 == 0:
#         r = r + "212"
#     else:
#         sum_2 = (r.count("1") + r.count("2") * 2) * 2
#         sum_2 = convert(sum_2,3)
#         r = r + sum_2
#     r = int(r,3)
#     if r > 490:
#         ans.append(r)
#
#
#
# print(min(ans))

# num = 729 ** 8 - 3 ** 18 + 85
# cnt = 0
# while num:
#     if num % 9 == 0: cnt += 1
#     num //= 9
# print(cnt)
from string import printable as alph
def convert(num,sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else "0"
from math import *
num = 283 ** 382 + 9 **  15 + 2 ** 3
cnt = 0
cnt_2 = 0
while num:
    if num % 14 == 11 : cnt += 1
    if num % 14 == 12: cnt_2 += 1
    num //= 14
print(abs(cnt - cnt_2))
