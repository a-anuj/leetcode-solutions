class Solution:
    def rob2(self, nums: list[int]) -> int:
        prev1 = prev2 = 0

        for num in nums:
            curr = max(prev1,prev2+num)
            prev2 = prev1
            prev1 = curr
        
        return prev1
    
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        return max(self.rob2(nums[:-1]),self.rob2(nums[1:]))
        