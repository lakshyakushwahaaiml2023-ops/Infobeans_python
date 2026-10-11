dict1 = {"a" : 10, "b" : 20}
dict2 = {"c" : 10, "d" : 20}

for key in dict1.keys():
    dict2.get(key, dict2.setdefault(key, dict1[key]))
print(dict2)