def reverse_string(s, pos):
    if pos == -1:
        return ""
    return s[pos] + reverse_string(s, pos - 1)

s = "Lakshya"
print(reverse_string(s, len(s) - 1))