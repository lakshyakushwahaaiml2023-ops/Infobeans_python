arr = [1,2,3,4,5,3,4,5,2]
print(f"Original list: {arr}")
flag = True

for i in range(len(arr)):
    if flag:
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                print(f"Duplicate element found: {arr[i]}")
                flag = False
                break
    else:
        break
else:
    print("No duplicate element found")
    