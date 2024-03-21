# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/


from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    rows = set()
    columns = set()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if (matrix[row][column] == 0):
                rows.add(row)
                columns.add(column)

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if (row in rows) or (column in columns):
                matrix[row][column] = 0

    print(matrix)





matrix_1 = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


print(setZeroes(matrix_1))
print(setZeroes(matrix_2))



