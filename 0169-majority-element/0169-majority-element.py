class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        set_n = set(nums)
        for i in set_n:
            if nums.count(i) > n/2:
                return i

        