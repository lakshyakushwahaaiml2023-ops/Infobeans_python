string = "aaaaabbccccdde"
res = {}
for i in string:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
ans = ""
for key, value in res.items():
    ans += f"{key}{value}"

print(f"Original String: {string}")
print(f"Compressed string: {ans}")