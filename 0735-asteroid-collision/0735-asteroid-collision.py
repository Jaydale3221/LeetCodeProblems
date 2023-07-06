class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result_stack = []  # Stores the remaining asteroids after collisions

        for asteroid in asteroids:
            collision_flag = 1

            # Check for collisions with the previous asteroids in the result stack
            while result_stack and result_stack[-1] > 0 and asteroid < 0:
                if abs(result_stack[-1]) > abs(asteroid):
                    collision_flag = 0  # No collision, asteroid destroyed
                    break
                elif abs(result_stack[-1]) < abs(asteroid):
                    result_stack.pop()  # Previous asteroid destroyed
                else:
                    result_stack.pop()  # Both asteroids destroyed (equal in size)
                    collision_flag = 0
                    break

            if collision_flag == 1:
                result_stack.append(asteroid)  # No collision, add asteroid to result stack

        return result_stack
