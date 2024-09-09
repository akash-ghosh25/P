def largest_element(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    
    return largest

array = [10, 5, 23, 8, 17]
print(f"The largest element in the array is: {largest_element(array)}")
