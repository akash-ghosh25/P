n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))

print("Before swap n1 =",n1,"& n2 =",n2)

n1 += n2
n2 = n1 - n2
n1-=n2

print("After swap n1 =",n1,"& n2 =",n2)