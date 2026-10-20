with open(r"../files/") as file:
    data = file.readline()

for i in "EU":
    data = data.replace(i,"A")

for i in "CDF":
    data = data.replace(i,"B")

data = data.replace(i, "")
for i in "AB": data = data.replace(i, "")
data = data.split()
print(len(max(data, key=len)))