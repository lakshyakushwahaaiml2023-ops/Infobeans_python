#Dutch Flag Algorithm

arr = [1,0,0,2,2,1,1,2,0,0,1]
print(f"Original array: {arr}")

start = 0
mid = 0
end = len(arr) - 1

while mid <= end:
    if arr[mid] == 0:
        arr[start], arr[mid] = arr[mid], arr[start]
        start +=1
        mid += 1
    elif arr[mid] == 1:
        mid+=1
    else:
        arr[mid], arr[end] = arr[end], arr[mid]
        end -= 1

print(f"Array after sorting: {arr}")