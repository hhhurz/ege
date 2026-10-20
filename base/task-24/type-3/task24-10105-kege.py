with open (r"../files/24_10105.txt") as data:
    data=data.readline()
data = data.replace("CD","C D")
data = data.split(" ")
ans = 0
for i in range(len(data)-160):
    line = "".join(data[i:i+161])
    ans = max(ans,len(line))
print(ans)
