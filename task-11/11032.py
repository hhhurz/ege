from math import log2,ceil

for l in range(1,100000):
    n = 52 + 963 + 10
    i = ceil(log2(n))
    I = ceil(l*i/8)
    if I * 2000 <= 693*1024:
        print(l)
