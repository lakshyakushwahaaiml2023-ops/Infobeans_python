arr = [1,0,0,1,0,1,1,0,1,0,1]
print(f"Original list: {arr}")
balance = 0
first_seen = {0: -1}
longest = 0

for i, value in enumerate(arr):
    balance += 1 if value == 1 else -1
    if balance in first_seen:
        longest = max(longest, i - first_seen[balance])
    else:
        first_seen[balance] = i

print("Longest subarray with equal 0s and 1s:", longest)