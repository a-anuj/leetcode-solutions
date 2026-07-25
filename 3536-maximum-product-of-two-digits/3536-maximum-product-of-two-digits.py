class Solution:
    def maxProduct(self, n: int) -> int:
        nums = list(str(n))
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort(reverse=True)
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] * nums[1] 