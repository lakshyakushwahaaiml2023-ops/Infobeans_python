d1 = {
    "a" : 10,
    "b" : 20,
    "c" : 30,
    "d" : 40,
    "e" : 50,
    "f" : 60
}

d2 = {
    "a" : 10,
    "b" : 200,
    "c" : 30,
    "d" : 400,
    "e" : 50
}

d1 = {key : value for key, value in d1.items() if d1[key] == d2.get(key) }
print(d1)