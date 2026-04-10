class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] +=1

            maxFreq = max(maxFreq,count[index])

            while right-left+1 - maxFreq > k:
                index_left = ord(s[left]) - ord('A')
                count[index_left] -=1
                left+=1
            ans = max(ans,right-left+1)
        return ans