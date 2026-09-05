class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            alive = True
            while alive and stack and ast < 0 and stack[-1] > 0:
                if abs(ast) < stack[-1]:
                    alive = False
                
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    alive = False

                else:
                    stack.pop()
            if alive:
                stack.append(ast)
        return stack
