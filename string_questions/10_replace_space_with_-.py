string = "My name is Lakshya"
res = ""
for i in string:
    if i != " ":
        res += i
    else:
        res += '-'

print(res)