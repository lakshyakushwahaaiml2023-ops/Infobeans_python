def reverse_words(string):
    words = string.split()[::-1]
    ans = ""
    for i in words:
        ans += i + " "
    return ans


string = "Lakshya is playing games"
print(reverse_words(string))