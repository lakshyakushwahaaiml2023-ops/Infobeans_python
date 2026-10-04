def rotate(arr):
    temp = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp

arr = [1,2,3,4, 5]
max_prod = 0
k = 0

while k < len(arr):
    for i in range(len(arr) - k + 1):
        prod = 1
        for j in range(i, i + k):
            prod *= arr[j]
        if prod > max_prod:
            max_prod = prod
    rotate(arr)
    k += 1

print(f"Max product sum is: {max_prod}")