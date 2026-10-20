with open(r'..\files\24_1866дз.txt') as file:
    data = file.readline()

cnt = 0
ans = 0
for i in range(len(data)-1):
     if data[i:1+2] == 'ad' or data[i:1+2] == 'da' :
        cnt = 1
     else:
         cnt += 1


     ans = max(ans,cnt)
print(ans)