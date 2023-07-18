# 100. Same Tree
# https://leetcode.com/problems/same-tree/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = [(p,q)]


        while stack:

            p,q = stack.pop()


            if (p and q) and p.val == q.val:

                stack.append([p.left, q.left])
                stack.append([p.right, q.right])

            elif p or q:

                return False

        return True



p_1 = TreeNode(1, TreeNode(2), TreeNode(3))
q_1 = TreeNode(1, TreeNode(2), TreeNode(3))
# Output: true

p_2 = TreeNode(1, TreeNode(2), None)
q_2 = TreeNode(1, None, TreeNode(2))
# Output: false

p_3 = TreeNode(1, TreeNode(2), TreeNode(1))
q_3 = TreeNode(1, TreeNode(1), TreeNode(2))
# Output: false     


t = Solution()
print(t.isSameTree(p_1, q_1))
t = Solution()
print(t.isSameTree(p_2, q_2))
t = Solution()
print(t.isSameTree(p_3, q_3))


