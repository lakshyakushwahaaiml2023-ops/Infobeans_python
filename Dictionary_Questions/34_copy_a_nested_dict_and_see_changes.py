d1 = {"Lakshya" : {"phy" : 20,
                   "chem" : 40,
                   "bio": 35},
    "Kapil" : {"phy" : 20,
                   "chem" : 40,
                   "bio": 35}
    
                   }

print(id(d1))
print(id(d1["Kapil"]))
d2 = d1.copy()
print(id(d2))
print(id(d2["Kapil"]))