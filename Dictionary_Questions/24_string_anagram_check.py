str1 = "listen"
str2 = "silent"

freq1 = {}
freq2 = {}

for i in str1:
    if i in freq1:
        freq1[i] += 1
    else:
        freq1[i] = 1

for i in str2:
    if i in freq2:
        freq2[i] += 1
    else:
        freq2[i] = 1

print("Anagram") if freq1 == freq2 else print("Not an anagram")