ans = []

for n in range(1,100000):
    r = f"{n:b}"
    if n % 8 == 0:
        r = r + r[-2:]
    else:
        r = r + f"{n % 8 * 2:b}"
    if int(r,2) > 3000:
        ans.append(n)
print(min(ans))