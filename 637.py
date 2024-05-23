# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description


from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        stack = [[0, root]]
        levels = defaultdict(list)

        while stack:
            
            level, node = stack.pop()
            levels[level].append(node.val)

            if node.left != None:
                stack.append([level+1, node.left])

            if node.right != None:
                stack.append([level+1, node.right])


        return [sum(v)/len(v) for k,v in levels.items()]


        

# [3,9,20,null,null,15,7]
root_1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, 
# and on level 2 is 11.
# Hence return [3, 14.5, 11].


# [3,9,20,15,7]
root_2 = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))
# Output: [3.00000,14.50000,11.00000]


root_3 = TreeNode(1, TreeNode(2), TreeNode(20))
# Output: [1.00000,11.00000]

print(Solution().averageOfLevels(root_1))
print(Solution().averageOfLevels(root_2))
print(Solution().averageOfLevels(root_3))

