'''Q1. Longest Substring Without Repeating Characters

Write a Python program to find the length of the longest substring that contains no repeating characters.

Example:
Input: abcabcbb
Output: 3

Explanation: "abc" is the longest substring.

'''

def solution(s):
    bucket = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in bucket:
            bucket.remove(s[left])
            left += 1

        bucket.add(s[right])

        cur_len = right - left + 1

        max_len = max(max_len, cur_len)

    return max_len

s = ""
print(solution(s))