d1 = {"a" : 10, "b" : 30, "c" : 50}
d2 = {"b" :40, "c" : 80, "d" : 100}

for i in d1.keys():
    if i in d2:
        print(i)