with open (r"../files/24_19254.txt") as data:
    data = data.readline()


data = data.replace("FSRQ","*** ***")
data = data.split(" ")
ans = 0

for i in range(len(data)-80):
    line = "".join(data[i:i+81]).replace("******","FSRQ")
    ans = max(ans,len(line))
print(ans)
































with open(r"../files/24_19254.txt") as data:
    data = data.readline()


data = data.replace("FRSQ","*** ***")
data = data.split(" ")
ans = 0
for i in range(len(data)-80):
    line = " ".join(data[i:i+81]).replace("******","FRSQ")
    ans = max(ans,len(line))

print(ans)





























with open(r"../files/24_19254.txt") as data:
    data = data.readline()

cnt = r = l = ans = 0
len_data = len(data)

while r < len_data:
    if cnt < 80 :
        if data[r:r+4] == "FRSQ":
            cnt +=1
    r +=1

else:

    l+=1