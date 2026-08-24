class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        maxSum = float("-inf")
        for i in nums:
            temp += i
            maxSum = max(maxSum,temp)
            if temp<0:
                temp = 0
        return maxSum

