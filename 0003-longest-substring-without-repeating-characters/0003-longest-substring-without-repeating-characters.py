class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = []
        size = 0

        for right in range(len(s)):
            while s[right] in window:
                window.pop(0)
                left+=1
            size = max(size,right-left+1)

            window.append(s[right])
        return size