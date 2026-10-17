def sec_most_freq_char(word):
    res = {}
    for i in word:
        res[i] = res.get(i,0) + 1
    max_count = word[0]
    sec_max = word[0]
    for key, value in res.items():
        if value > res[max_count]:
            sec_max = max_count
            max_count = key
        elif (value < res[max_count])and (value > res[sec_max]):
            sec_max = key
    return sec_max

word = "Lakshya Kushwaha"

print(f"Second Most frequent character: {sec_most_freq_char(word)}")
