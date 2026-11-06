with open(r'../files/24_11667 (1).txt') as data:
    data = data.readline()

r = l = cnt = ans = 0
for r in range(len(data)-7):
    if data[r:r+8] == "INFINITY":
        cnt +=1
    while cnt > 1000:
        if data[l:l+8] == "INFINITY": cnt -=1
        l +=1
    if cnt == 1000:
        ans = max(ans,r-l+8)
print(ans)