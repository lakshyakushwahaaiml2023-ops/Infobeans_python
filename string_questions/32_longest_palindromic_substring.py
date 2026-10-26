

# substrings = set()

# for right in range(len(string)):
#     for j in range(right +1, len(string)+1):
#         substrings.add(string[right: j])


# max_len_sub = string[0]
# for i in substrings:
#     start = 0
#     end = len(i) - 1
#     while start < end:
#         if i[start] != i[end]:
#             break
#         start += 1
#         end -= 1
#     else:
#         if len(i) > len(max_len_sub):
#             max_len_sub = i

# print(max_len_sub)
def longest_palindrome(s):
    start = 0
    max_len = 0
    for i in range(len(s)):
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        c_len = right - left - 1
        if max_len < c_len:
            max_len = c_len
            start = left + 1
    for i in range(len(s)):
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        c_len = right - left - 1
        if max_len < c_len:
            max_len = c_len
            start = left + 1

    return s[start: start + max_len]

string = "babaddab"
print(longest_palindrome(string))

        