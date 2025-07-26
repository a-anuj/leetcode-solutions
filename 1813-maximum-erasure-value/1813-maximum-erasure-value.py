class Solution(object):
    def maximumUniqueSubarray(self, nums):
        res = nums[0]
        l = 0
        numSet = set()
        curSum=0

        for r in range(len(nums)):
            while nums[r] in numSet:
                curSum-=nums[l]
                numSet.remove(nums[l])
                l+=1
                
            numSet.add(nums[r])
            curSum += nums[r]

            res = max(res,curSum)
        return res

