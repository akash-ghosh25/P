def find_sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

array = [1, 2, 3, 4, 5]
print(f"The sum of the array is: {find_sum(array)}")
