dict = {"a" : 10, "b" : 20, "c" : 10, "d" : 20}
seen = set()
res = {}

for key, value in dict.items():
    if value not in seen:
        res[key] = value
        seen.add(value)
print(res)