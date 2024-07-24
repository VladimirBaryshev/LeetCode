# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/


from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in matrix:
            if m[0] <= target <= m[-1]:
                # print(m, target)
                return target in m

        return False


matrix_1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target_1 = 3
# Output: true


matrix_2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target_2 = 13
# Output: false

matrix_3 = [[1]]
target_3 = 1

print(Solution().searchMatrix(matrix_1, target_1))
print(Solution().searchMatrix(matrix_2, target_2))
print(Solution().searchMatrix(matrix_3, target_3))


