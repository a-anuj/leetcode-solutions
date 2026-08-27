class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * len(nums)):
            temp = i % n
            while stack and nums[temp] > nums[stack[-1]]:
                prev = stack.pop()
                result[prev] = nums[temp]
            
            if i<n:
                stack.append(i)
        return result