class Solution(object):
    
    def count_vowels(self,string):
        count = 0
        for i in string.lower():
            if i in "aeiou":
                count +=1
        return count

    def maxVowels(self, s, k):
        window_count = self.count_vowels(s[:k])
        res = window_count
        vowels = "aeiou"

        for i in range(k,len(s)):
            if s[i] in vowels:
                window_count+=1
            if s[i-k] in vowels:
                window_count-=1
            res = max(res,window_count)
        return res 
        