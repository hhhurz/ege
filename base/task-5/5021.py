from string import printable as alph



def convert(num,sys):
    res = ""
    while num:
        res+= alph[num % sys]
        num //= sys
    return res[::-1] if res  else "0"







ans =[]
for N in (1,100000):
    R = convert(N,3)
    if N % 3 == 0:
        R = "1" + "02"
    else:
        R = R + convert(N % 3 * 4,3)
    R = int(R,3)
    if R < 199:
        ans.append(R)
print(R)
