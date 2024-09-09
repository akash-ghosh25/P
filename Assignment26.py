lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input())
    lst.append(ele)

print("List:", lst)

if n > 1:
    lst[0], lst[n-1] = lst[n-1], lst[0]

print("After interchange of first and last elements in the list:",lst)
