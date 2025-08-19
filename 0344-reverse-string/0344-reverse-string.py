class Solution(object):
    def reverseString(self, s):
        n = len(s)
        left = 0
        right = n-1

        while left<right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return s
        