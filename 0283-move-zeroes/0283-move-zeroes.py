class Solution(object):
    def moveZeroes(self, nums):
        lastNonZero = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[lastNonZero] = nums[lastNonZero],nums[i]
                lastNonZero+=1
        return nums