def reverse_words(string):
    return " ".join(string.split()[::-1])


string = "Lakshya is learning Python"
print(reverse_words(string))