class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i<j:
                    if abs(nums[i]-nums[j]) == k:
                        count += 1
        
        return count