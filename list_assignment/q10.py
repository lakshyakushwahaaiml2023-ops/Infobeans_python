arr = [1, 2, 3, 4, 5, 6, 7]
k = 4
k = k % len(arr) 
print(f"Original list: {arr}")

def reverse_arr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

reverse_arr(arr, 0, len(arr) -1)
reverse_arr(arr, 0, k - 1)
reverse_arr(arr, k, len(arr) - 1)

print(f"Rotated list after {4} positions: {arr}")