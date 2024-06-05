# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right =self.buildTree(preorder[index+1:], inorder[index+1:])

        return root




preorder_1 = [3,9,20,15,7]
inorder_1 = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

preorder_2 = [-1]
inorder_2 = [-1]
# Output: [-1]

print(Solution().buildTree(preorder_1, inorder_1))
print(Solution().buildTree(preorder_2, inorder_2))