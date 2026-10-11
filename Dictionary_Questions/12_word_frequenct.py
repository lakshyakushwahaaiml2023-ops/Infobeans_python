string = "python is easy and python is powerful and easy to learn python is fun to learn and powerful"
res = {}

word = ""

for i in string:
    if i != " ":
        word += i
    else:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
        word = ""

print(res)