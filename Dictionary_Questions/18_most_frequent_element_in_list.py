nums = [1, 2, 2, 1, 4, 1, 8, 9 , 0 , 7 , 5 , 6 , 7 , 8 , 8 , 8 , 1, 1]
freq = {}

most_freq = nums[0]

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    if freq[i] > freq[most_freq]:
        most_freq = i
print(f"Most frequent element in list => {most_freq} : {freq[most_freq]} times")