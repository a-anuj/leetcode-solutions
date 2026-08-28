class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window = 0
        minval = float('inf')

        for right in range(len(nums)):
            window += nums[right]

            while window >= target:
                minval = min(minval,right-left+1)
                window -= nums[left]
                left += 1
        
        return minval if minval!=float('inf') else 0