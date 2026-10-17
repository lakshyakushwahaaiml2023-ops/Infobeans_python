def reverse_every_word(string):
    words = string.split()
    words = [i[::-1] for i in words]
    ans = ""
    for i in words:
        ans += i + " "
    return ans

string = "My name is Lakshya"
ans = reverse_every_word(string)
print(ans)