# 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

from typing import List

def minOperations(boxes: str) -> List[int]:

    '''

        Solution ideas
        num_steps = 1+1 + (1+1)
        ones_counts = 1 + 1 + 1

        Input: boxes = "00101 1 "
        Output: [11,8,5,4,3,4]


        Потом справа налево

    '''
    result = [0 for i in range(len(boxes))]

    # print(result)
    # print(boxes)
    nums_steps = 0
    ones_counts = 0

    for i, s in enumerate(boxes):

        nums_steps += ones_counts
        if s == '1':
            ones_counts += 1
        # print(i, s, nums_steps, ones_counts)
        result[i] += nums_steps
    
    # print(nums_steps)
    # print(ones_counts)
    L = len(boxes)-1
    nums_steps = 0
    ones_counts = 0
    for i, s in enumerate(boxes[::-1]):
        # print(L-i, s)
        nums_steps += ones_counts
        if s == '1':
            ones_counts += 1
        # print(i, s, nums_steps, ones_counts)
        result[L-i] += nums_steps

    return result



boxes_1 = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, 
# and move one ball from the second box to the third box in one operation.

boxes_2 = "001011"
# Output: [11,8,5,4,3,4]

print(minOperations(boxes_1))
print(minOperations(boxes_2))



