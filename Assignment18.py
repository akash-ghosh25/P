def rec_sum(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return rec_sum(n-1) + n
    
n = int(input("Enter the range: "))
print("sum of natural numbers is = ",rec_sum(n))