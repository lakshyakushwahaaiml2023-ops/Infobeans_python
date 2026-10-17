string = "a3b4c5de1"
res = ""
word = ""
for i in string:
    if i.isnumeric():
        res += word * int(i)
        word = ""
    else:
        word += i

print(res)