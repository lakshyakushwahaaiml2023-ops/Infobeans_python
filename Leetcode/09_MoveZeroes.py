def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1

    while left < len(nums):
        nums[left] = 0
        left += 1

nums = [0,5,1,0,2,0,5,1,0]
move_zeroes(nums)
print(nums)
