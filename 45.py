# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/description/


from typing import List


def jump(nums: List[int]) -> int:
    
    counter = 0
    l = r = 0

    while r < len(nums)-1:
        
        max_i = 0
        
        for i in range(l, r+1):
            max_i = max(max_i, i+nums[i])
        l = r + 1 
        r = max_i
        counter += 1

    return counter



nums_1 = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. 
# Jump 1 step from index 0 to 1, then 3 steps to the last index.

nums_2 = [2,3,0,1,4]
# Output: 2

nums_3 = [1,2]
# output: 1

print(jump(nums_1), '\n')
print(jump(nums_2), '\n')
print(jump(nums_3), '\n')





