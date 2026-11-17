class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        stack = []

        for index,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = index - top
            
            stack.append(index)
        
        return result