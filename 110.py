# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def isBalanced(self, root: TreeNode) -> bool:

        if not root:
            return True
        
        self.answer = True
        
        def dfs(root):

            l, r = 0, 0

            if root.left:
                l += dfs(root.left)

            if root.right:
                r += dfs(root.right)

            if abs(r-l) > 1:
                self.answer = False
                
            # print(root.val, l, r)
            return max(r,l) + 1

        dfs(root)
        return self.answer


        
        



root_1 = TreeNode(3,TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7))) # Output: true

root_2 = TreeNode(1,TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)) # Output: false

root_3 = TreeNode() # Output: true

t = Solution()
print(t.isBalanced(root_1))
t = Solution()
print(t.isBalanced(root_2))
t = Solution()
print(t.isBalanced(root_3))


