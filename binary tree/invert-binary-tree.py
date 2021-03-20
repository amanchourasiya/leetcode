# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.util(root)

    def util(self, root):
        if root is None:
            return root
        
        left = self.util(root.right)
        right = self.util(root.left)
        root.left = left
        root.right = right
        return root
