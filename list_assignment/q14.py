arr = [-1, 2, -1, 3, 2]

print(f"Original list: {arr}")

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            break
    else:
        print("First non repeating element is:", arr[i])
        break
else:
    print("No non repeating element found")