arr = [1,2,3,4,5,6,12,40]
target = 40
start = 0
end = len(arr) - 1
while True:
    if start > end:
        print(f"Element not found")
        break

    mid = (start + end)//2

    if arr[mid] == target:
        print(f"Element found at {mid} index")
        break
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid + 1