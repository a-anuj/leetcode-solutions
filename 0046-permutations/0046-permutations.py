class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = [False] * n
        temp = []
        ans = []

        def backtrack(n,freq,temp):
            if len(temp) == n:
                ans.append(temp[:])
                return 
            for i in range(n):
                if not freq[i]:
                    freq[i] = True

                    temp.append(nums[i])
                    backtrack(n,freq,temp)
                    temp.pop()
                    freq[i] = False
        
        backtrack(n,freq,temp)
        return ans