class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []

        for ast in asteroids:
            alive = True
            while alive and ast < 0 and stack and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()
                elif stack[-1] == -ast:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(ast)

        return stack