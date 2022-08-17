file = open("info.txt", "r")
data = file.read()
print(data)

list_info = data.split("\n")
print(list_info)
data_1 = {}
for i in list_info:
    ",".join(data_1[i])
print(data_1)


