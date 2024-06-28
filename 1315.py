# 1315. Sum of Nodes with Even-Valued Grandparent
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        result = 0
        stack = [[root,-1,-1]] # node, parent, grandparent ## TreeNode, int, int

        while stack:
            cur_node, parent, gparent = stack.pop()
            
            if gparent % 2 == 0:
                result += cur_node.val

            if cur_node.left:
                stack.append([cur_node.left, cur_node.val, parent])
            if cur_node.right:    
                stack.append([cur_node.right, cur_node.val, parent])

        return result

            