# 669. Trim a Binary Search Tree

from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        if root == None:
            return None

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if low <= root.val <= high:
            # print(root.val)
            return root

        if root.left != None:
            return root.left

        if root.right != None:
            return root.right
        



root_1 = TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=2))
low_1 = 1
high_1 = 2
# Output: [1,null,2]

root_2 = TreeNode(val=3, left=TreeNode(val=0, right=TreeNode(val=2, left=TreeNode(val=1))), right=TreeNode(val=4))
low_2 = 1
high_2 = 3
# Output: [3,2,null,1]


# print(Solution().trimBST(root_1, low_1, high_1))
print(Solution().trimBST(root_2, low_2, high_2))