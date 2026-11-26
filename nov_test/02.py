'''Q2. String Anagram

Write a program to check whether two given strings are anagrams of each other.

Anagrams contain the same characters with the same frequency, but in a different order.
Input:
String 1: listen
String 2: silent

Output: Anagram


Do not use sorted().'''

def anagram_check(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            return False
    return True

    
def anagram_check2(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch in freq:
            freq[ch] -= 1
        else:
            return False
    for ch in s1:
        if freq[ch] != 0:
            return False
    return True

s1 = "silent"
s2 = "Liste"

print(anagram_check2(s1, s2))