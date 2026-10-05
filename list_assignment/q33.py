arr = [1,3,2,5,4,2,6]
target = 50
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element found at {i} index")
        break
else:
    print(f"Element not found")