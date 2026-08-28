class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for ast in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and ast < 0:
                if stack[-1] > abs(ast):
                    alive = False
                
                elif stack[-1] == abs(ast):
                    stack.pop()
                    alive = False
                
                elif stack[-1] < abs(ast):
                    stack.pop()
            
            if alive:
                stack.append(ast)
        return stack