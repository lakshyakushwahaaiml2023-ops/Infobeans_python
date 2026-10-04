arr = [4, 5, 1, 2, 2, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 7]

longest = 1
current = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i - 1] + 1:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

print(longest)
