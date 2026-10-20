with open(r"../files/") as file:
    data = file.readline()
#data = *****bab*****da
vow = "A,E,U"
con = "B,C,D,F"


ans , cnt , i = 0
len_data = len(data)-2
while i < len_data:
    if data[i] in con and data[i+1] in vow and data[i+2] in con:
        cnt +=1
        i +=3
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)
