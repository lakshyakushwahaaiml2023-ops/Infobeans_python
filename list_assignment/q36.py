# Insertion sort
# Start from index 1 and compare the value at index 1 with
# previous value, if the previous value is greater than the current value
# then swap the values and move to the next index and repeat the process

arr = [4,1,2,6,5,0,8,2,6,1]
print(f"Original array: {arr}")

for i in range(1, len(arr)):
    temp = arr[i]
    j = i-1
    while j >= 0:
        if arr[j] > temp:
            arr[j+1] = arr[j]
        else:
            break
        j-=1
    arr[j+1] = temp

print(f"Sorted Array: {arr}")
