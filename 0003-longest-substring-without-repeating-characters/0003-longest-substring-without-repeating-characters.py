class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        charSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res
        
        