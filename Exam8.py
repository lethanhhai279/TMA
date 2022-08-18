import math
n = int(input('Nhap n: '))
for i in range(2,int(math.sqrt(n))):
    if n % i == 0:
        print(f'So {n} khong la so nguyen to!')
    else:
        print(f'So {n} la so nguyen to!')
