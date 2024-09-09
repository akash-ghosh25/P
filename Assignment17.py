n = int(input("Enter the value: "))
sum = 0
for i in range(1, n+1):
    sum = sum+(i**2)

print("Sum of squares of first", n, "natural numbers is = ",sum)