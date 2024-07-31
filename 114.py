# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/


from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:

        """
        Do not return anything, modify root in-place instead.
        """

        curr = root
        while curr:
            if curr.left:
                runner = curr.left
                while runner.right:
                    runner = runner.right
                runner.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right




# [1,2,5,3,4,null,6]
root_1 = TreeNode(
                    val=1, 
                    left=TreeNode(
                                    val=2,
                                    left=TreeNode(val=3),
                                    right=TreeNode(val=4)
                                ),
                    right=TreeNode(
                                    val=5,
                                    left=None,
                                    right=TreeNode(val=6)
                                )
                )
# Output: [1,null,2,null,3,null,4,null,5,null,6]

root_2 = []
# Output: []

root_3 = [0]
# Output: [0]


print(Solution().flatten(root_1))