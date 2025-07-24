class Solution(object):
    def maxAbsoluteSum(self, nums):
        maxSum,minSum = 0,0
        curSum = 0
        res = 0

        for n in nums:
            temp = n+maxSum
            maxSum = max(n+maxSum,n)
            minSum = min(n,n+minSum)

            res = max(res,abs(maxSum),abs(minSum))
        return res
        