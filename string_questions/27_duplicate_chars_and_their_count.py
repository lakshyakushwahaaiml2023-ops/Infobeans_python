def duplicate_chars(string):
    res = {}
    for i in string:
        res[i] = res.get(i,0) + 1
    return {key: value for key,value in res.items() if value >= 2 }
string = "My name is Lakshya Kushwaha"
ans = duplicate_chars(string)
print(ans)