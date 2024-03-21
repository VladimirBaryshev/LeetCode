# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/


from typing import List

def mapper(matrix, start, end, step):

    print("YO")

    for i in range(start, end, step):
        print(i)


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    
    result = []

    left, right = 0, len(matrix[0])-1
    top, bottom = 0, len(matrix)-1

    while True:

        if left > right:
            break
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        if top > bottom:
            break
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        if left > right:
            break
        for i in range(right, left-1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        if bottom < top:
            break
        for i in range(bottom, top-1, -1):
            result.append(matrix[i][left])
        left += 1

    return result



matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

matrix_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

print(spiralOrder(matrix_1))
print(spiralOrder(matrix_2))
