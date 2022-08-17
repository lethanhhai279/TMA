import time

name = str(input("Nhap ten: "))
current_age = int(input("Nhap tuoi: "))

data = time.ctime(time.time())
# print(data)
current_year = int(data.split(" ")[-1])
# print(type(current_year))
year_100 = current_year + (100 - current_age)

print(f"Ban {name} se tron 100 tuoi vao nam {year_100}")