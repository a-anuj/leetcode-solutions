class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = []
        windowLeng = 0

        for i in range(len(s)):
            if s[i] in window:
                while s[i] in window:
                    window.pop(0)
                    left+=1
            window.append(s[i])
            windowLeng = max(windowLeng, len(window))

        return windowLeng 