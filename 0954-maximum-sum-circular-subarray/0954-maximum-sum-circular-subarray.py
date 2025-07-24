class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = 0
        curMin,minSub = 0,nums[0]
        curMax,maxSub = 0,nums[0]

        for n in nums:
            total_sum += n

            curMax = max(n,curMax+n)
            maxSub = max(maxSub,curMax)

            curMin = min(n,curMin+n)
            minSub = min(curMin,minSub)

        if maxSub<0:
            return maxSub
        else:
            return max(maxSub,total_sum-minSub)
                