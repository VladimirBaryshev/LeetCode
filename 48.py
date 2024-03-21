# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/


from typing import List


def rotate(matrix: List[List[int]]) -> None:

    """
    Do not return anything, modify matrix in-place instead.
    """
    # print(matrix)

    l = 0
    r = len(matrix)-1

    while l < r:
        for i in range(r - l):

            lli, lir, rri, ril = matrix[l][l+i], matrix[l+i][r], matrix[r][r-i], matrix[r-i][l]
            matrix[l][l+i], matrix[l+i][r], matrix[r][r-i], matrix[r-i][l] = ril, lli, lir, rri

        l += 1
        r -= 1

    # print(matrix)




matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

print(rotate(matrix_1))
# print(rotate(matrix_2))
