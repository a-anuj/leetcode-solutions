class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        left = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in window:
                while s[i] in window:
                    window.pop(0)
                    left+=1
            window.append(s[i])
            ans = max(ans,len(window))
        return ans