lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input())
    lst.append(ele)

print("Before reverse: ",lst)
for i in range(n//2):
    t = lst[i]
    lst[i] = lst[n-i-1]
    lst[n-i-1] = t

print("After reverse: ",lst)
