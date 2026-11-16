def singleNum(nums):
    ans = 0
    for i in nums:
        ans ^= i
    return ans

nums = [1,4,7,2,4,7,2]
print(singleNum(nums))