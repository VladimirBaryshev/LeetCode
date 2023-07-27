# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_bin_tree(root):

    level = 0
    result = dict()
    stack = [[level, root]]

    while stack:

        l, root = stack.pop()

        if root != None:

            # print(l, root.val)
            if l in result.keys():
                result[l].append(root.val)
            else:
                result[l] = []
                result[l].append(root.val)
            stack.append([l+1, root.left])
            stack.append([l+1, root.right])
            

    # return result, [result[k][0] for k in result.keys()]
    return [result[k][0] for k in result.keys()]


root_1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
# Output: [1,3,4]

root_2 = TreeNode(1, None, TreeNode(3))
# Output: [1,3]

root_3 = None
# Output: []

root_4 = TreeNode(1, TreeNode(2))
# Output: [1,2]

root_5 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
# Output:[1,3,4]

print(right_bin_tree(root_1))
print(right_bin_tree(root_2))
print(right_bin_tree(root_3))
print(right_bin_tree(root_4))
print(right_bin_tree(root_5))



