def isomorhicStrings(s1, s2):
    dict1 = {}
    dict2 = {}
    if len(s1) != len(s2):
        return False
    for a, b in zip(s1, s2):
        if a in dict1 and dict1[a] != b:
            return False
        if b in dict2 and dict2[b] != a:
            return False
        dict1[a] = b
        dict2[b] = a
    return True

s1 = "add"
s2 = "egq"

print(isomorhicStrings(s1, s2))