class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # left = []
        # right = []
        # for i in range(len(nums)):
        #     left.append(sum(nums[:i]))
        #     right.append(sum(nums[i+1:]))
        
        # op = []
        # for i in range(len(left)):
        #     op.append(abs(left[i]-right[i]))
        # return op

        total = sum(nums)
        left_sum = 0
        ans = []
        for num in nums:
            total -= num
            ans.append(abs(left_sum-total))
            left_sum+=num
        
        return ans
