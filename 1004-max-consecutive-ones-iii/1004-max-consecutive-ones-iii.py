class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        count = 0

        for right in range(len(nums)):
            if nums[right]==1:
                count+=1

            window_length = right-left+1

            while window_length-count > k:
                if nums[left]==1:
                    count-=1
                left+=1
                window_length-=1
            ans = max(ans,window_length)
        
        return ans