class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float('inf')
        maxProfit = 0

        for i in prices:
            if i<minVal:
                minVal = i
            else:
                maxProfit = max(maxProfit,i-minVal)

        return maxProfit