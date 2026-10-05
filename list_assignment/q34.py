#selection sort
#Find the smallest value in every iteration
#Keep the value at its right place and swap the original
# value at that index with the min value

arr = [4,1,2,6,5,0,8,2,6,1]
print(f"Original array: {arr}")
for i in range(len(arr) - 1):
    min_val = arr[i]
    j = i + 1
    min_index = i
    while j < len(arr):
        if arr[j] < min_val:
            min_val = arr[j]
            min_index = j
        j += 1
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(f"Sorted array: {arr}")