# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        r = collections.defaultdict(list)
        q = [(0, root)]

        while q:

            level, node = q.pop(0)

            if node != None:
                
                r[level].append(node.val)
                q.append((level+1, node.left))
                q.append((level+1, node.right))

        return r.values()