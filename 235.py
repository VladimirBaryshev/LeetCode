# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:

    '''
        We will rely upon the invariant of the BST to solve the exercise. 
        We know that the left subtree of each node contains nodes with smaller values 
        and the right subtree contains nodes with greater values. 
        We also know that if two nodes, x and y, are on different subtrees 
        of a node z (one in the left portion and one in the right portion), 
        then x and y have z as the lowest common ancestor. 
    '''

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while True:

            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


root_1 = TreeNode(6,TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
p_1 = TreeNode(2)
q_1 = TreeNode(8)
# Output: 6


root_2 = TreeNode(6,TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
p_2 = TreeNode(2)
q_2 = TreeNode(4)
# Output: 2


root_3 = TreeNode(2, TreeNode(1))
p_3 = TreeNode(2)
q_3 = TreeNode(1)
# Output: 2     

t = Solution()
print(t.lowestCommonAncestor(root_1, p_1, q_1).val)
t = Solution()
print(t.lowestCommonAncestor(root_2, p_2, q_2).val)
t = Solution()
print(t.lowestCommonAncestor(root_3, p_3, q_3).val)







