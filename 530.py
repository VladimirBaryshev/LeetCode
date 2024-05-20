# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        stack = [root]
        vals = []
        min_diff = 10**5

        while stack:

            node = stack.pop(0)

            if node.left != None:
                stack.append(node.left)

            if node.right != None:
                stack.append(node.right)

            if node.val != None:
                
                if len(vals) != 0:
                    for i in vals:
                        min_diff = min(abs(node.val - i), min_diff)
                vals.append(node.val)


        return min_diff





        

# [4,2,6,1,3]
root_1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))

# Output: 1

# [1,0,48,null,null,12,49]
root_2 = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
# Output: 1


print(Solution().getMinimumDifference(root_1))
print(Solution().getMinimumDifference(root_2))



