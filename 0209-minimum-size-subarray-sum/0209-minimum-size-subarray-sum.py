class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        left = 0
        minLen = float('inf')

        for right in range(len(nums)):
            window+=nums[right]
            
            while(window>=target):
                minLen = min(minLen,right-left+1)
                window-=nums[left]
                left+=1

        if minLen == float('inf'):
            return 0
        else:
            return minLen