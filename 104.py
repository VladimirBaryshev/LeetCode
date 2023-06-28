# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104. Maximum Depth of Binary Tree

from typing import Optional

# root_1 = [3,9,20,null,null,15,7]
# Output: 3

# root_2 = [1,null,2]
# Output: 2


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = 0

        stack = [[root, 1]]

        while len(stack) > 0:

            node, level = stack.pop()
            if node:
                max_depth = max(max_depth, level)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])

        return max_depth



# root_1 = [3,9,20,null,null,15,7]
root_1_t_case = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
t = Solution()
print(t.maxDepth(root_1_t_case))
# Output: 3



# root_2 = [1,null,2]
root_2_t_case = TreeNode(1, None, TreeNode(2))
t = Solution()
print(t.maxDepth(root_2_t_case))
# Output: 2


# root_3 = []
root_3_t_case = TreeNode()
t = Solution()
print(t.maxDepth(root_3_t_case))
# Output: 0




