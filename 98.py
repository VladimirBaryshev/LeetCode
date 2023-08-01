# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        stack = [[root, 2**31, -2**31-1]]

        while stack:

            node, mustLess, mustGreater = stack.pop()
            print(node.val, 'mustLess', mustLess, 'mustGreater', mustGreater)

            if node.val >= mustLess or node.val <= mustGreater:
                return False

            if node.left is not None:
                stack.append([node.left, min(mustLess, node.val), mustGreater])

            if node.right is not None:
                stack.append([node.right, mustLess, max(mustGreater, node.val)])

        return True


root_1 = TreeNode(2, TreeNode(1), TreeNode(3))
# Output: true

root_2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
# Output: false

root_3 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
# Output: false

root_4 = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6)))
# Output: true


# t = Solution()
# print(t.isValidBST(root_1))

# t = Solution()
# print(t.isValidBST(root_2))

# t = Solution()
# print(t.isValidBST(root_3))

t = Solution()
print(t.isValidBST(root_4))