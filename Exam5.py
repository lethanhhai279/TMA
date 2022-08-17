from tokenize import Double


n = input("Nhap so: ")

while(n is str):
    print(f"So {n} khong thoa man")

if int(n) % 2 == 0:
    print(f"So {n} la so chan")
elif int(n) % 2 != 0:
    print(f"So {n} la so le")
else:
    print(f"So {n} khong thoa man!!")