class Solution(object):
    def maximumWealth(self, accounts):
        maxval = 0

        for i in accounts:
            count = 0
            for j in i:
                count+=j
            maxval = max(maxval,count)
        return maxval
        