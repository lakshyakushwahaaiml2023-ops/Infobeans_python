'''Q4. String Compression

Write a program to compress a string by replacing consecutive repeated characters with the character followed by its frequency.
Input: aaabbccccdaa

Output: a3b2c4d1a2'''

def compress(s):
    ans = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            ans = ans + f"{s[i-1]}{count}"
            count = 1

    ans = ans + f"{s[-1]}{count}"

    return ans

s = "aaabbccccdaa"

print(compress(s))
s = "abcd"
print(compress(s))
s = "a"
print(compress(s))

s = "1"
print(compress(s))

