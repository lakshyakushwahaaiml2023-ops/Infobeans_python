def remove_duplicate(nums):
    pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[pos] = nums[i]
            pos += 1

nums = [1,2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8]
remove_duplicate(nums)
print(nums)