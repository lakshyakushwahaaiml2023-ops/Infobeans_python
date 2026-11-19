'''Q3. Longest Palindromic Substring

Write a program to find the longest palindromic substring in a given string.
Input: babad
Output: bab


Note: aba is also a valid answer.'''

def longest(s):
    start = 0
    maxLen = 0

    for i in range(len(s)):
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        curLen = right - left - 1

        if maxLen < curLen:
            start = left + 1
            maxLen = curLen

    for i in range(len(s)):
        left = i
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        curLen = right - left - 1
        
        if maxLen < curLen:
            start = left + 1
            maxLen = curLen

    return s[start : start + maxLen]

s = "babad"
print(longest(s))
s = "babaddab"
print(longest(s))
