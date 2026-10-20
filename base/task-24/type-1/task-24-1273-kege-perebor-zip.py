with open(r"../files/24_1273.txt") as file:
    data = file.readline()

ans,cnt = 0,2
for i in zip(data, data[1:], data[2:]):
    if ''.join(i) != "XYZ":
        cnt += 1
    else:
        cnt = 2
    ans = max(ans, cnt)
print(ans)
