ans = []
for N in range(10000):
    R = f"{N:b}"
    if R.count("1") %  2 == 0:
        R = R + "0"
        R = 
