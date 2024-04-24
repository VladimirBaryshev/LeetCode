# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/


from typing import Optional
from collections import defaultdict



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        stack = [(0, root)]
        levels = defaultdict(list)

        while stack:
            
            level, cur = stack.pop(0)
            if cur != None:
                levels[level].append(cur.val)
                stack.append((level+1, cur.left))
                stack.append((level+1, cur.right))
            else:
                levels[level].append(None)

        
        while level > 0:
            t = levels[level]
            if t[:len(t)//2] == list(reversed(t[len(t)//2:])):
                level -= 1
            else:
                return False

        return True



# root_1 = [1,2,2,3,4,4,3]
root_1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
# Output: true

# root_2 = [1,2,2,null,3,null,3]
root_2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
# Output: false

print(Solution().isSymmetric(root_1))
print(Solution().isSymmetric(root_2))

