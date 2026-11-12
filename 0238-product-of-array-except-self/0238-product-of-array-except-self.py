class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        
        result = [1]*n
        curr = 1
        for i in range(len(nums)):
            result[i]=curr
            curr = curr * nums[i]

        curr = nums[n-1]
        for i in range(len(nums)-2,-1,-1):
            result[i] *= curr
            curr = curr * nums[i]

        return result