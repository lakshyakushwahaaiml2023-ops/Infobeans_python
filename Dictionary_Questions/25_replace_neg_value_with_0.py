values = {
    "a" : 1,
    "b" : -3,
    "c" : -5,
    "d" : 5,
    "e" : -7
}

for key in values:
    if values[key] < 0:
        values[key] = 0
print(values)