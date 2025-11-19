class Solution(object):
    def numberGame(self, nums):
        arr = []
        nums.sort()
        while nums:
            alice = nums[0]
            bob = nums[1]
            nums = nums[2:]
            arr.append(bob)
            arr.append(alice)
        return arr