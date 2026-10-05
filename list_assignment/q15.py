arr = [1,0,0,1,0,1,1,0,1,0,1]
print(f"Original list: {arr}")

count = 0

for i in range(len(arr)):
    sum = 0

    for j in range(i, len(arr)):
        if arr[j] == 0:
            sum -= 1
        if arr[j] == 1:
            sum += 1
        if sum == 0:
            count += 1

print(f"Number of sub-lists having equal 0's and 1's: {count}")