# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

from typing import List

class Solution:

    def sortedSquares(self, A: List[int]) -> List[int]:

        l_pointer = 0
        r_pointer = len(A)-1
        A = [i**2 for i in A]
        result = [0 for i in A]

        while l_pointer != r_pointer:
            if A[l_pointer] >= A[r_pointer]:
                result[r_pointer-l_pointer] = A[l_pointer]
                l_pointer += 1
            else:
                result[r_pointer-l_pointer] = A[r_pointer]
                r_pointer -= 1

        result[r_pointer-l_pointer] = A[r_pointer]
        return result



nums_1 = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

nums_2 = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

print(Solution().sortedSquares(nums_1))
print(Solution().sortedSquares(nums_2))