# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.depth(root)
        
    def depth(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.depth(root.left), self.depth(root.right))