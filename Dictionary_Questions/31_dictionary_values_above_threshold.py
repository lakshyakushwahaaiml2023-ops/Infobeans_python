d1 = {
    "a" : 10,
    "b" : 20,
    "c" : 30,
    "d" : 40,
    "e" : 50,
    "f" : 60
}
thresh = 40

d1 = {key : value for key, value in d1.items() if d1[key] >= thresh}
print(d1)