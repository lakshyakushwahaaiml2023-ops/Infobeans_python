def stringMinus(s, t):
    for ch in t:
        if s.count(ch) != t.count(ch):
            return ch

s1 = "abbca"
s2 = "cabbaa"
print(stringMinus(s1, s2))    