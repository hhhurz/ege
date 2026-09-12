# file = open(r'../files/24_1975,txt')
# data = file
# file.close() # закрывает поток, не закрыл поток - жопаааа
# r-убирает конфликт со специальными символами
#.. - выход из папки


with open(r'..\files\24_1975.txt') as file:
    data = file.readline()




cnt, ans = 1, 0

# len-считает кол-во символов
# range-диапазон
for i in range(len(data)):
    if data[i] + data[i+1] == 'PP' or data[i:1 + 2] == 'PP':
        ans = max(ans,cnt)
        cnt = 1
    else:
        cnt += 1
print(ans)