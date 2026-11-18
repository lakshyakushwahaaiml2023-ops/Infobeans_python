def fourSum(nums, target):
    nums.sort()
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums) - 2):
            if i > i + 1 and nums[i] == nums[i-1]:
                continue
            rem = target - nums[i] - nums[j]
            left = j + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == rem:
                    return [i, j, left, right], [nums[i], nums[j], nums[left], nums[right]]
                elif nums[left] + nums[right] > rem:
                    right -= 1
                else:
                    left += 1
nums = [1,2,3,4,5,6,7,8,9,10]
print(fourSum(nums, 34))