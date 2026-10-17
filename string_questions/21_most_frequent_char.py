def most_freq_char(word):
    res = {}
    max_count = word[0]
    for i in word:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
        if res[max_count] < res[i]:
            max_count = i
    return max_count

word = "aaabbccbbaabsbdbdbbdsasssssssssssssssssss"

print(f"Most frequent character: {most_freq_char(word)}")
