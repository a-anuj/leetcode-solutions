class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = float('-inf')
        left = 0
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            if right-left+1 == k:
                avg = max(avg,window_sum/k)
                window_sum -= nums[left]
                left+=1
        return avg