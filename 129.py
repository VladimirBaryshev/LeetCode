# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150


from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        stack = [[root, ""]]
        res = []

        while stack:
            root, val = stack.pop(0)

            if root and root.left:
                stack.append([root.left, val+str(root.val)])

            if root and root.right:
                stack.append([root.right, val+str(root.val)])

            if root.left == None and root.right == None:
                res.append(val+str(root.val))
            
        
        return sum((int(i) for i in res))
    
            

        