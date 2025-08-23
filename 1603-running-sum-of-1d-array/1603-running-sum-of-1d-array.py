class Solution(object):
    def runningSum(self, nums):
        result = [nums[0]]
        sum_val = nums[0]
        for i in range(1,len(nums)):
            sum_val += nums[i]
            result.append(sum_val)
        return result
        