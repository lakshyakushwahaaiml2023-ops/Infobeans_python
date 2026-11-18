def longest_substring_without_repeating_chars(s):
    left = 0
    start = 0
    bucket = set()
    maxLen = 0
    for right in range(len(s)):
        while s[right] in bucket:
            bucket.remove(s[left])
            left += 1

        bucket.add(s[right])
        curLen = right - left + 1
        if curLen > maxLen:
            start = left
            maxLen = curLen
    return maxLen, s[start: start + maxLen]

s = "abcdcdba"
print(longest_substring_without_repeating_chars(s))