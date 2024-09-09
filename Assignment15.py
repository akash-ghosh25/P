def prime_num(n):
    if(n<2):
            return False
    for i in range(2,(n//2)+1):
        if(n % i == 0):
            return False

    return True
        

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
for i in range(start,end+1):
    if(prime_num(i)):
        print(i)