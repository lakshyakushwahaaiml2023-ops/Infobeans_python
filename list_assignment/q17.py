arr = [4, 2, 3, 1, 6, 0]

sum = 0
seen_sum = []

for i in arr:
    sum += i
    if sum == 0 or sum in seen_sum:
        print("Yes")
        break
    seen_sum.append(sum)
else:
    print("No")