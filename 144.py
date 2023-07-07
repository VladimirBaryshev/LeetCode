# https://leetcode.com/problems/binary-tree-preorder-traversal/
# 144. Binary Tree Preorder Traversal


# Edge cases and constraints:
# len(nodes) >= 0
# left child might be absent (Null) in test case


# Solution ideas:
# Definition class of binary tree
# preorder traversal DFS



from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def preorder_traverse(root: Optional[TreeNode]) -> list[int]:
        
        result = []
        stack = []

        if len(root) == 0:
            return result
        stack.append(root[0])

        while len(stack) > 0:
            node = stack.pop(-1)
            node_val, node_l, node_r = node.val, node.left, node.right
            result.append(node_val)
            
            if node_r != None:
                stack.append(node_r)
            if node_l != None:
                stack.append(node_l)

        return result

        
# input = [1, None, 2, 3] # 1,2,3
input_ = [TreeNode(1, None, TreeNode(2, TreeNode(3), None))]



print(Solution.preorder_traverse(input_))