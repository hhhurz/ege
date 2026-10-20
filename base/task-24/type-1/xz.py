from itertools import product
combs = product("ABCDEF", repeat= 3)
combs = ["".join(i) for i in product("ABCDEF", repeat = 3)]
#*comb - показывает все комбинации а не посылает нас куда в итератор( можно воспользоваться только один раз)
# ''.join(i) - работает со строками
#*comb работает с кортежами


with open(r"../files/") as file:
    data = file.readline()
#data = ****a b****a*****abcd

ans, cnt = 0, 2
for line in zip(data, data[1:], data[2:]): # line  уже кортеж
    if ''.join(i) not in combs:
        cnt +=1
    else:
        cnt = 2
    ans = max(ans,cnt)
print(ans)