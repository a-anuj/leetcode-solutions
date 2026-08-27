class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = {}

        for num in nums2:
            while stack and num>stack[-1]:
                top = stack.pop()
                result[top] = num
            stack.append(num)

        
        ans = [result.get(num,-1) for num in nums1]
        return ans