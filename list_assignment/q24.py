arr = [1,2,3,4,5]
print(f"Original array: {arr}")
arr[0], arr[len(arr)-1] = arr[len(arr) - 1], arr[0]
print(f"New array: {arr}")