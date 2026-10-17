def count_chars(word):
    res = {}
    for i in word:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

ans = count_chars("Lakshya Kushwaha is Back")

for key, value in ans.items():
    print(f"{key} : {value} times")