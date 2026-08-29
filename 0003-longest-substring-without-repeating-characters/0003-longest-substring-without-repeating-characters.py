class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []

        maxlen = 0

        for right in range(len(s)):
            while s[right] in window:
                window.pop(0)
            
            window.append(s[right])
            maxlen = max(maxlen,len(window))
        return maxlen
