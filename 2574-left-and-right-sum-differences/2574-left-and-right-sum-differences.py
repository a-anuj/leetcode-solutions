class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        for i in range(len(nums)):
            left.append(sum(nums[:i]))
            right.append(sum(nums[i+1:]))
        
        op = []
        for i in range(len(left)):
            op.append(abs(left[i]-right[i]))
        return op