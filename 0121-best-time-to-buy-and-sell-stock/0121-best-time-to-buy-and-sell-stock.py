class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        maxProfit = 0
        for i in prices:
            if i < minimum:
                minimum = i
            else:
                maxProfit = max(maxProfit, i-minimum)
        return maxProfit