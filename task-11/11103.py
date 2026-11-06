from math import log2,ceil

for l in range(1,100000):
    n = 80
    i = ceil(log2(n))
    I = ceil(l * i / 8)
    if 1234567* I > 24 * 1024 * 1024:
        print(l)
        break 