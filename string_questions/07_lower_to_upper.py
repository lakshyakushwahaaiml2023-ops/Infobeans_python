string = "My name is Lakshya 2004"
res = ""
for i in string:
    if ord(i) >= 97 and ord(i) <= 122:
        res += chr(ord(i) - 32)
    else:
        res += i
print(res)