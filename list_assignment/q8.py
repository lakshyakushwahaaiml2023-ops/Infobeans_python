arr = [1, -1, 3, 2, -7, -5, 11, 6]
print(f"Original list: {arr}")
res = []
for i in arr:
    if i > 0:
        res.append(i)
for i in arr:
    if i < 0:
        res.append(i)
print(f"Rearranged list: {res}")