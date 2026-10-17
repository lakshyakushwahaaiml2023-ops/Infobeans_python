string = "abcabcbabcdeed"
left = 0
bucket = set()
max_len = 0
low = 0
end = 0
for right in range(len(string)):
    while left <= right and (string[right] in bucket):
        bucket.remove(string[left])
        left += 1
    bucket.add(string[right])
    if (right - left + 1) > max_len:
        max_len = right - left + 1
        low = left
        end = right
print(f"Longest substring without repetition : {string[low:end+1]} , Length: {max_len}")
