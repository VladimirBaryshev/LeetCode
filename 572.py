# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, tree: TreeNode, sub_tree: TreeNode) -> bool:

        if not sub_tree: 
            return True

        if not tree:
            return False

        if self.sameTree(tree, sub_tree):
            return True

        return self.isSubtree(tree.left, sub_tree) or self.isSubtree(tree.right, sub_tree)


    def sameTree(self, tree, sub_tree):

        if not tree and not sub_tree:
            return True

        if (tree and sub_tree) and tree.val == sub_tree.val:
            return self.sameTree(tree.left, sub_tree.left) and self.sameTree(tree.right, sub_tree.right)

        return False


root_1 = TreeNode(3,TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot_1 = TreeNode(4, TreeNode(1), TreeNode(2))
# Output: true

root_2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subRoot_2 = TreeNode(4, TreeNode(1), TreeNode(2))
# # Output: false

t = Solution()
print(t.isSubtree(root_1, subRoot_1))

t = Solution()
print(t.isSubtree(root_2, subRoot_2))


