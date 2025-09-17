class Solution(object):
    def mostWordsFound(self, sentences):
        maxLen = 0
        for i in sentences:
            maxLen = max(maxLen,len(i.split()))
        return maxLen
        