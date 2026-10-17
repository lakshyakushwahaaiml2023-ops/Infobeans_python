def binary_search_recurssion(arr, start, end, target):
    if start > end:
        return -1
    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search_recurssion(arr, start, mid-1, target)
    return binary_search_recurssion(arr, mid + 1, end, target)

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            print(f"{target} found at index {mid}")
            return
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print("Target not found")

arr = [1,2,3,4,5,6,7,7,8,9]
start = 0
end = len(arr) - 1
target = 9
binary_search(arr, target)
print(binary_search_recurssion(arr, start, end, target))