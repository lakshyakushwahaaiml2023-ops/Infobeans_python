string = "aabbsbabsbbac"
res = {}
for i in string:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
for key, value in res.items():
    if value == 1:
        print(f"{key} occurs once first")
        break