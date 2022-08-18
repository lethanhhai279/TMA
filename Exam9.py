list_fibo = [0,1]
n = int(input("Nhap n: "))
def fib(n):
    a = 0
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        list_fibo.append(c)
    print(list_fibo)
fib(n)


def Fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))


number = int(input("Enter the Range Number: "))
list_fibonacci = []
for i in range(0, number):
    list_fibonacci.append(Fibonacci(i))
print(list_fibonacci)