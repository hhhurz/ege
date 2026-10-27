ans = []
for N in range(1,1000000):
    R = f"{N:b}"
    if R[-1] == "0":
        R ="10" + R
    else:
        R = "1" + R +"01"
    R = int(R,2)
    if R > 441:
        ans.append(N)
        ans = ans + [N]
print(min(ans))
