string = "abcabcbb"
left = 0
bucket = set()
for right in range(len(string)):
    while string[right] in bucket:
        bucket.remove(string[left])
        left += 1
    bucket.add(string[right])

print(len(bucket))
