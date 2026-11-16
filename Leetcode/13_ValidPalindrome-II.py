def validPalindrome(s1):

    def isPalindrome(left, right):
        while left < right:
            if s1[left] != s1[right]:
                return False
            left += 1
            right -= 1
        return True
    left = 0
    right = len(s1) - 1

    while left < right:
        if s1[left] != s1[right]:
            return isPalindrome(left+1, right) or isPalindrome(left, right - 1)
        left += 1
        right -= 1
    return True

s = "aba"
print(validPalindrome(s))