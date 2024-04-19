# 566. Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/description/


from typing import List


class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        vector = []
        
        for row in mat:
            vector.extend(row)


        new_mat = []

        cur = 0
        while cur < r*c:
            cur_row = vector[cur:cur+c].copy()
            new_mat.append(cur_row)
            cur += c

        return new_mat



mat_1 = [[1,2],[3,4]]
r_1 = 1
c_1 = 4
# Output: [[1,2,3,4]]


mat_2 = [[1,2],[3,4]]
r_2 = 2
c_2 = 4
# Output: [[1,2],[3,4]]

print(Solution().matrixReshape(mat_1, r_1, c_1))
print(Solution().matrixReshape(mat_2, r_2, c_2))
