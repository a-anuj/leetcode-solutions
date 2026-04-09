class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxVal = float('-inf')

        while left<=right:
            area = min(height[left],height[right]) * (right-left)

            maxVal = max(area,maxVal)

            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxVal
        