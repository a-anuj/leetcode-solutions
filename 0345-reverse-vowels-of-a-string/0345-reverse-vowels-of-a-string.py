class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        found_vowels = ""

        for i in s:
            if i in vowels:
                found_vowels+=i

        new=""
        j=len(found_vowels)-1
        for i in range(len(s)):
            if s[i] in vowels:
                new+=found_vowels[j]
                j-=1
            else:
                new+=s[i]
        return new