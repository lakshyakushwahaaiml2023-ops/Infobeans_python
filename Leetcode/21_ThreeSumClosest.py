class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minDist = float('inf')
        closest = None
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                absMin = abs(target - summ)
                if absMin < minDist:
                    minDist = absMin
                    closest = summ
                if summ == target:
                    return summ
                elif summ > target:
                    right -= 1

                else:
                    left += 1
        return closest
        

        