class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(i):
            if i == n:
                ans.append(nums[:])
                return
            
            for j in range(i,n):
                nums[i],nums[j] = nums[j],nums[i]
                backtrack(i+1)
                nums[j],nums[i] = nums[i],nums[j]
            
        backtrack(0)
        return ans