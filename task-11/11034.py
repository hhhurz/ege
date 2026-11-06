from math import log2,ceil
l = 248
for n in range(1,100000):
    i = ceil(log2(n))
    I = ceil(248 * i / 8)
    if I*75600 > 16 * 1024 * 1024:
        print(n)
        break

