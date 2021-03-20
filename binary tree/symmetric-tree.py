# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.util(root.left, root.right)
        
        
    def util(self, left, right):
        if left is None and right is None:
            return True

        if (left is None and right is not None) or (left is not None and right is None):
            return False

        if left.val != right.val:
            return False
        
        return self.util(left.left, right.right) and self.util(left.right, right.left)
        
