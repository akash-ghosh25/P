lst = [10,20]
print("Before swap: ",lst)
temp = lst[0]
lst[0] = lst[len(lst)-1]
lst[len(lst)-1] = temp
print("After swap: ",lst)
