arr = [4, 2, 3, 1, -6, 0]

sum = 0
seen_sum = []

for i in arr:
    sum += i
    seen_sum.append(sum)

max = seen_sum[0]
for i in seen_sum:
    if i > max:
        max = i

print(f"Maximum subarray sum is: {max}")