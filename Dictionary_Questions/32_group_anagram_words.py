words =  ["eat", "tea", "bat", "ate"]
res = {}

for i in words:
    freq = {}
    for j in i:
        if j in freq:
            freq[j] += 1
        else:
            freq[j] = 1
    res[i] = freq
print(res)