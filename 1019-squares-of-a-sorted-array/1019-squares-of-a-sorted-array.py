class Solution(object):
    def sortedSquares(self, nums):
        result = [0] * len(nums)
        n = len(nums)
        l,r = 0,n-1

        for i in range(n-1,-1,-1):
            if abs(nums[l]) > abs(nums[r]):
                val = nums[l]
                l+=1
            else:
                val = nums[r]
                r-=1
            result[i] = val ** 2
        return result