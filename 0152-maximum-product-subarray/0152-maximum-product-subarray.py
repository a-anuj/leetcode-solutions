class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        maxNums,minNums = 1,1

        for n in nums:
            if n==0:
                maxNums,minNums = 1,1
                continue
            
            temp = n * maxNums
            maxNums = max(n*maxNums,n*minNums,n)
            minNums = min(temp,n*minNums,n)
            res = max(res,maxNums)
        
        return res
        