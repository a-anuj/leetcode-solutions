class Solution(object):
    def maxSubArray(self, nums):
        curSum = 0 
        maxSum = float("-inf")

        for i,num in enumerate(nums):
            curSum += num
            maxSum = max(maxSum,curSum)
            if curSum<0:
                curSum = 0
            
        return maxSum