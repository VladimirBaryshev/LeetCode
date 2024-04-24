# 112. Path Sum
# https://leetcode.com/problems/path-sum/description


from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root == None:
            return False

        stack = [(root.val, root)]

        # print(stack)

        while stack:
            cur_sum, cur_node = stack.pop()

            if cur_sum == targetSum and cur_node.right == None and cur_node.left == None:
                return True

            if cur_node.left and cur_node.left.val != None:
                stack.append((cur_node.left.val+cur_sum, cur_node.left))

            if cur_node.right and cur_node.right.val != None:
                stack.append((cur_node.right.val+cur_sum, cur_node.right))    

        return False



# root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
root_1 = TreeNode(5, TreeNode(4, left=TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1))))
targetSum_1 = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.


# root = [1,2,3]
root_2 = TreeNode(1, TreeNode(2), TreeNode(3))
targetSum_2 = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# root = []
root_3 = TreeNode()
targetSum_3 = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
 
root_4 = TreeNode(val=-2, left=TreeNode(val=6, left=TreeNode(val=0, left=None, right=None), right=TreeNode(val=-6, left=None, right=None)), right=None)
targetSum_4 = 4
# Output: true
print(Solution().hasPathSum(root_1, targetSum_1))
print(Solution().hasPathSum(root_2, targetSum_2))
print(Solution().hasPathSum(root_3, targetSum_3))
print(Solution().hasPathSum(root_4, targetSum_4))


