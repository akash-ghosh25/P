lst = []
sum = 0
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input())
    lst.append(ele)

for i in range(n+1):
    sum += i

print("Sum of elements in list is = ",sum)
