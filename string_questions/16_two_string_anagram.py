string1 = "Listen"
string2 = "silenk"

f1 = {}
f2 = {}

if len(string1) != len(string2):
    print("Not Anagram")
else:
    for i in string1.lower():
        if i in f1:
            f1[i] += 1
        else:
            f1[i] = 1
    for i in string2.lower():
            if i in f2:
                f2[i] += 1
            else:
                f2[i] = 1
    if f1 == f2:
        print("Anagram")
    else:
        print("Not Anagram")