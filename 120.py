# 120. Triangle
# https://leetcode.com/problems/triangle/description/


from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:


        res = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):

                res[j] = min(res[j], res[j+1]) + triangle[i][j]

                print(i, j, triangle[i][j], res)

        return res[0]



triangle_1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

triangle_2 = [[-10]]
# Output: -10

print(Solution().minimumTotal(triangle_1))
print(Solution().minimumTotal(triangle_2))
