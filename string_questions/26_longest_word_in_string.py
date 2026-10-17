def longest_word(string):
    words = string.split()
    max_len_word = words[0]
    for word in words:
        if len(word) > len(max_len_word):
            max_len_word = word
    return max_len_word

string = "My name is Lakshya Kushwaha"
print(f"Max length word in \"{string}\" : {longest_word(string)}")