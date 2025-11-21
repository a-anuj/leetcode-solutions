class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
        for i in s+t:
            result ^= ord(i)
        return chr(result)