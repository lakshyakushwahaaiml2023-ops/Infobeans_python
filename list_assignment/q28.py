arr = [1,2,3,4,5,6,7,8,9,10, 11, 12]
start = 0
end = len(arr) - 1
target = 12
while True:

    if start > end:
        print("Element not found")
        break
    mid = (start + end) // 2

    if arr[mid] == target:
        print(f"Element found at index: {mid}")
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
    