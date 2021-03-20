# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        self.val = root.val
        return self.util(root)
        
    def util(self, root):
        if root is None:
            return True
        
        if root.val != self.val:
            return False
        
        return self.util(root.left) and self.util(root.right)