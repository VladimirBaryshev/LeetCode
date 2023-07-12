# https://leetcode.com/problems/diameter-of-binary-tree
# 543. Diameter of Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0
        self.dfs(root)

        return self.diameter


    def dfs(self, node):

        if node == None:
            return 0

        left_h = self.dfs(node.left)
        right_h = self.dfs(node.right)

        self.diameter = max(self.diameter, left_h+right_h)

        return max(left_h,right_h)+1





# Input: 
# root = [1,2,3,4,5] 
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

input_1 = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))
t = Solution()
print(t.diameterOfBinaryTree(input_1))

