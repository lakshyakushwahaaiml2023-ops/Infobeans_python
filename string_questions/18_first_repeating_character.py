def first_repeating_char(word):
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            if word[i] == word[j]:
                return i
    else:
        return -1

word = "ProgrammingP"
ans = first_repeating_char(word)
if ans != -1:
    print(f"First repeating character: {word[ans]}")
else:
    print(f"No repeating characters in {word}")
