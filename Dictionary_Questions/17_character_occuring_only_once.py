string = "aaabcbeadbcbaadaff"
chars = {}

for i in string:
    if i in chars:
        chars[i] += 1
    else:
        chars[i] = 1
for i in chars:
    if chars[i] == 1:
        print(f"{i} : {chars[i]}")
        break