# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/


# Edges and constraints:
# Each val in tree is unique
# tree[i] positive num
# number of nodes in tree  >= 0
#   If 0 TreeNode is None



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        stack = [root]
        while stack:
            
            tmp = stack.pop()
            if tmp.val == val:
                return tmp
            elif tmp.val < val:
                if tmp.right:
                    stack.append(tmp.right)
                else:
                    return None
            if tmp.val > val:
                if tmp.left: 
                    stack.append(tmp.left)
                else:
                    return None

        return None
