# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/



from typing import Optional
from collections import defaultdict



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        stack = [root]

        if stack[0].val == None:
            return 0

        count = 1
        while stack:

            cur = stack.pop(0)
            if cur.left != None:
                count += 1
                stack.append(cur.left)
            if cur.right != None:
                count += 1
                stack.append(cur.right)

        return count




# root = [1,2,3,4,5,6]
# Output: 6
root_1 = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)), right=TreeNode(val=3, left=TreeNode(val=6)))

# root = []
# Output: 0
root_2 = TreeNode()

# root = [1]
# Output: 1
root_3 = TreeNode(val=1)


print(Solution().countNodes(root_1))
print(Solution().countNodes(root_2))
print(Solution().countNodes(root_3))