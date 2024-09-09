def fib(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input("Enter the range: "))
if(n<1):
    print("Invalid input!")
else:
    for i in range(1,n+1):
        print(i,"th Fibonacci is = ",fib(i))