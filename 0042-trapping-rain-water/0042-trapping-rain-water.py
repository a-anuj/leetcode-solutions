class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        temp = height[0]
        result = 0

        for i in range(n):
            if height[i] > temp:
                temp = height[i]
                leftMax[i] = temp
            else:
                leftMax[i] = temp
        
        temp = height[n-1]
        for i in range(n-1,-1,-1):
            if height[i] > temp:
                temp = height[i]
                rightMax[i] = temp
            else:
                rightMax[i] = temp
        
        for i in range(n):
            result += min(leftMax[i],rightMax[i]) - height[i]
        return result
