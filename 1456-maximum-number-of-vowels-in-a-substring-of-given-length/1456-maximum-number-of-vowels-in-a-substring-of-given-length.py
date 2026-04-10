class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = s[:k]
        
        count = 0
        for i in window:
            if i in "aeiou":
                count +=1
        maxVal = count

        for right in range(k,len(s)):
            if s[right] in "aeiou":
                count += 1
            if s[right-k] in "aeiou":
                count -= 1
        
            maxVal = max(maxVal,count)

        return maxVal

