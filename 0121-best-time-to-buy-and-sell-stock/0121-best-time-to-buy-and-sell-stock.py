class Solution(object):
    def maxProfit(self, prices):
        answer = 0
        minval = max(prices)
        for i,num in enumerate(prices):
            if num<minval:
                minval = num
            else:
                answer = max(answer,num-minval)
        return answer