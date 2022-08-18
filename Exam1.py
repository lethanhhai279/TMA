import info
data = info.d
name = input('Nhap ten: ')
for i in data:
    if name == i:
        print(f"Ngay sinh cua {i} la {data[i]}")