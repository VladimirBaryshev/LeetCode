# 1022. Sum of Root To Leaf Binary Numbers


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = []
        def dfs(root,path):
            if root == None:
                return 
            if root.left:
                dfs(root.left,path+str(root.left.val))
            if root.left == None and root.right == None:
                #cur = path + str(root.val)
                total.append(int(path,2))
            if root.right:
                dfs(root.right,path+str(root.right.val))
        dfs(root,str(root.val))
        return sum(total)

# [1,0,1,0,1,0,1]
root_1 = TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=0), right=TreeNode(val=1)), right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=1)))
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


# [0]
root_2 = TreeNode(val=0)
# Output: 0

# [1,1]
root_3 = TreeNode(val=1, left=TreeNode(val=1), right=TreeNode())

print(Solution().sumRootToLeaf(root_1))
print(Solution().sumRootToLeaf(root_2))
print(Solution().sumRootToLeaf(root_3))