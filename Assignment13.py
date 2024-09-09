n = int(input("Enter value to check armstrong number: "))
count = 0
sum = 0

t = n
while(t>0):
    count +=1
    t //= 10

t = n
while(t>0):
    digit = t%10
    sum = sum+(digit ** count)
    t //= 10

if(n == sum):
    print(n,"is an armstrong number")
else:
    print(n,"not an armstrong number")