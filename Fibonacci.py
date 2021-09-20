def Fibonacci(n):
    if n == 0:
       return 0

    elif n == 1:
        return 1
    else:
        s = Fibonacci(n - 1) + Fibonacci(n - 2)
        return s

n = int(input("Enter the No. for Fibonacci series: "))
print(Fibonacci(n))
