#Bubble Sort
#In every iteration find the biggest element and
#keep it at last

arr = [4,1,2,6,5,0,8,2,6,1]
print(f"Original array: {arr}")

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

print(f"Sorted array: {arr}")