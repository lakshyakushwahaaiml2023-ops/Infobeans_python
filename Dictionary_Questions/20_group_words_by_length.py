words = ["Lakshya", "Diksha", "Riya", "Ishant", "Krishna", "Ram", "Sam", "Kate", "Mike"]
res = {}

for i in words:
    key = len(i)
    if key in res:
        res[key].append(i)
    else:
        res[key] = [i]
print(res)