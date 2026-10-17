string = "babad"

substrings = set()

for right in range(len(string)):
    for j in range(right +1, len(string)+1):
        substrings.add(string[right: j])


max_len_sub = string[0]
for i in substrings:
    start = 0
    end = len(i) - 1
    while start < end:
        if i[start] != i[end]:
            break
        start += 1
        end -= 1
    else:
        if len(i) > len(max_len_sub):
            max_len_sub = i

print(max_len_sub)