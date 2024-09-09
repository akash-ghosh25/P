n = int(input("Enter the value: "))

fact = 1

for i in range(2,n+1):
    fact *= i

print("Factorial of",n,"is = ",fact)