# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        result = []
        stack = [[root, False]]

        while stack:

            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                result.append(node.val)

            else:
                stack.append([node.left, False])
                stack.append([node, True])
                stack.append([node.right, False])

        return result[-k]



root_1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
k_1 = 1
# Output: 1

root_2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
k_2 = 3
# Output: 3

t = Solution()
print(t.kthSmallest(root_1, k_1))

t = Solution()
print(t.kthSmallest(root_2, k_2))







