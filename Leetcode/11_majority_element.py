def majority(nums):
    major = nums[0]
    count = 0
    for i in range(len(nums)):
        if nums[i] == major:
            count += 1
        elif count > 0:
            count -= 1
        else:
            major = nums[i]
            count = 1
    return major

nums = [3,2,3,2,2,2]
print(majority(nums))