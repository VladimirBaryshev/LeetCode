# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


class Solution:

    def climbStairs(self, n: int) -> int:

        count_combinations = 0

        possible_stairs = [1, 2]

        stack = [1, [1]], [2, [2]]

        while stack:
            
            cur_sum, cur = stack.pop()

            if cur_sum < n:
                for s in possible_stairs:
                    stack.append([cur_sum+s, cur[::] + [s]])

            elif cur_sum == n:
                # print(cur)
                count_combinations += 1

        return count_combinations

        


n_1 = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

n_2 = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

n_3 = 4
n_4 = 35

print(Solution().climbStairs(n_1))
print(Solution().climbStairs(n_2))
print(Solution().climbStairs(n_3))
print(Solution().climbStairs(n_4))


