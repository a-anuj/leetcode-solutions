class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        lst = [len(str(s)) for s in nums]
        ans = 0
        for i in lst:
            if i%2==0:
                ans+=1
        return ans