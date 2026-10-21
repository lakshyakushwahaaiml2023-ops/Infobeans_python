arr = [-4, 2, 3, -1, -6, 0,-6]

prod = 1
seen_prod = []

for i in arr:
    prod *= i
    seen_prod.append(prod)

max = seen_prod[0]
for i in seen_prod:
    if i > max:
        max = i

print(max)