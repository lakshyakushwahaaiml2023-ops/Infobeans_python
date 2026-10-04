arr = [1,2,6,4,5,6,7,6,9]
print(f"Original list: {arr}")
target = 7
count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] + arr[j] == target and i != j:
            count += 1

print(f"Number of pairs that sum to {target}: {count}")