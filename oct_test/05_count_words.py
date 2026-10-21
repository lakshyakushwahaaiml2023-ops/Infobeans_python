sen = "Python is easy and Python is powerful"
res = {}
word = ""
for ch in sen:
    
    if ch != " ":
        word += ch
    else:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
        word = ""
if word in res:
    res[word] += 1
else:
    res[word] = 1

print(res)