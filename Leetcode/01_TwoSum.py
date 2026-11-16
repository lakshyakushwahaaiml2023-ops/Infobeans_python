def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in seen:
            return [seen[rem], i]
        seen[nums[i]] = i
    else:
        return -1

nums = [1,4,2,6,9,10,3]
target = 13
print(twoSum(nums, target))