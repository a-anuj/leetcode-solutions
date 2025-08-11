class Solution(object):
    def sortedSquares(self, nums):
        result = []
        for i in nums:
            result.append(i**2)

        return sorted(result)