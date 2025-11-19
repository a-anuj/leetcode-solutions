class Solution(object):
    def getSneakyNumbers(self, nums):
        temp = []
        res = []
        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                res.append(i)
        return res