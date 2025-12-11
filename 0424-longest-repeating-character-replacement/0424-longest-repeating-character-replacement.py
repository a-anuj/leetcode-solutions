class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count = [0] * 26
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index]+=1
            maxFreq = max(maxFreq,count[index])

            window_length = right-left+1
            while window_length-maxFreq > k:
                count[ord(s[left])-ord('A')]-=1
                left+=1
                window_length-=1
            ans = max(ans,window_length)
        return ans
