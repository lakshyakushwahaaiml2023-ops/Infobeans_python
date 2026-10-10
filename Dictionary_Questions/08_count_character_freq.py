str = "aaabbcccddde"
res = {}
for i in str:
    if i in res.keys():
        res[i] += 1
    else:
        res[i] = 1
print(res)