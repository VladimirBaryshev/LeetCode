# 55. Jump Game
# https://leetcode.com/problems/jump-game/description/



from typing import List



def canJump(nums: List[int]) -> bool:

    goal = len(nums)-1

    for i in range(len(nums)-1, -1, -1):
        # print(goal, i, nums[i])
        if goal <= i + nums[i]:
            goal = i

    return goal == 0




nums_1 = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

nums_2 = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

print(canJump(nums_1))
print('\n')
print(canJump(nums_2))

