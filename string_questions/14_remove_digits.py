string = "Ramanujan Number is 1729...HeHe"
res = ""
for i in string:
    if not i.isnumeric():
        res += i
print(res)