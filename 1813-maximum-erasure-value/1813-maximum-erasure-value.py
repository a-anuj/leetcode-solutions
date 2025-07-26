class Solution(object):
    def maximumUniqueSubarray(self, nums):
        res = nums[0]
        l = 0
        numSet = set()

        for r in range(len(nums)):
            while nums[r] in numSet:
                numSet.remove(nums[l])
                l+=1
            numSet.add(nums[r])

            res = max(res,sum(numSet))
        return res