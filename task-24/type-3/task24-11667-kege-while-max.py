with open(r"../files/24_11667 (1).txt") as data:
    data = data.readline()

r = l = cnt = ans = 0
len_data = len(data)

while r < len_data:
    if cnt <= 160:
        if data [r:r+2] == "INFINITY":
            cnt += 1
        r +=1
    else:
        if data[l:l+2] == "INFINITY":
            cnt -= 1
        l +=1
    ans = max(ans, r-l+(6 if r in range(len_data - 8, len_data + 1) else 0 ))

print(ans)
