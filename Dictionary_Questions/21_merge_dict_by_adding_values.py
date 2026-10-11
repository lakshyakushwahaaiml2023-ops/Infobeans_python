d1 = {"a" : 10, "b" : 20, "c" : 30}
d2 = {"c" : 20, "b" : 5, "d": 40, "e" : 50}

for key, value in d1.items():
    d2[key] = d2.get(key, 0) + value
print(d2)