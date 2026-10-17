def remove_dup(word):
    ans = ""
    seen = set()
    for i in word:
        if i not in seen:
            ans += i
            seen.add(i)
    return ans

word = "Lakshya Kushwaha"

print(f"After removing duplicates: {remove_dup(word)}")