operator = input("Enter operator: ")
n1 = float(input("Enter first value: "))
n2 = float(input("Enter second value: "))


if(operator == '+'):
    print(n1,"+",n2,"=",n1+n2)
elif(operator == '-'):
    print(n1,"-",n2,"=",n1-n2)
elif(operator == '*'):
    print(n1,"*",n2,"=",n1*n2)
elif(operator == '/'):
    print(n1,"/",n2,"=",n1/n2)
else:
    print("Invalid input")