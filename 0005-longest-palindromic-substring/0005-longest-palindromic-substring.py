class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxi = ""
        def expand(left,right):
            while left>=0 and right <len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)

            res = odd if len(odd)>len(even) else even
            maxi = maxi if len(maxi) > len(res) else res
        return maxi