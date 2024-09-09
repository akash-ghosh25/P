def fib(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input("Enter the value: "))
if(n<1):
    print("Invalid input!")
else:
    print(n,"th Fibonacci is = ",fib(n))