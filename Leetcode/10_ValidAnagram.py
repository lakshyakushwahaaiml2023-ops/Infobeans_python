def validAnagram(s1, s2):
    # freq = {}
    # for ch in s1:
    #     freq[ch] = freq.get(ch, 0) + 1

    # for ch in s2:
    #     if ch in freq:
    #         freq[ch] -= 1
    #     else:
    #         return False
    # for ch in s1:
    #     if freq[ch] != 0:
    #         return False
    # return True

    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            return False
    return True
        
s1 = "listen"
s2 = "silent"
print(validAnagram(s1, s2))