class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        temp = [sum(i) for i in accounts]
        return max(temp)