# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not postorder or not inorder:
            return None
        
        node = TreeNode(postorder[-1])
        root_index_inorder = inorder.index(postorder[-1])

        node.left = self.buildTree(inorder[:root_index_inorder], postorder[:root_index_inorder])
        node.right = self.buildTree(inorder[root_index_inorder+1:], postorder[root_index_inorder:-1])

        return node



inorder_1 = [9,3,15,20,7]
postorder_1 = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

inorder_2 = [-1]
postorder_2 = [-1]
# Output: [-1]

print(Solution().buildTree(inorder_1, postorder_1))
print(Solution().buildTree(inorder_2, postorder_2))
