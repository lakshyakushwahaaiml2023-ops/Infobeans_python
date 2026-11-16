def maxSum_subarray(nums):
    curSum = nums[0]
    maxSum = nums[0]

    start = 0
    end = 0
    tempStart = 0

    for i in range(1, len(nums)):

        if nums[i] > curSum + nums[i]:
            curSum = nums[i]
            tempStart = i
        else:
            curSum += nums[i]

        if curSum > maxSum:
            maxSum = curSum
            start = tempStart
            end = i

    return f"Max Sum: {maxSum} --> {nums[start:end+1]}"


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSum_subarray(nums))
