class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        temp = nums.copy()
        nums.reverse()
        return temp+nums