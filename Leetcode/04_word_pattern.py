def wordPattern(pattern, string):
    words = string.split()
    if len(pattern) != len(words):
        return False
    dict1 = {}
    dict2 = {}
    for ch, word in zip(pattern, words):
        if ch in dict1 and dict1[ch] != word:
            return False
        if word in dict2 and dict2[word] != ch:
            return False
        dict1[ch] = word
        dict2[word] = ch    
    return True

pattern = "abbac"
string = "dog cat cat dog elephant"
print(wordPattern(pattern, string))