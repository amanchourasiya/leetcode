# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        i = 0
        for j in range(1, len(preorder)):
            if preorder[j] > preorder[0]:
                i = j
                break
        if i != 0:
            root.right = self.bstFromPreorder(preorder[i:])
        if i == 0:
            i = len(preorder) 
        root.left = self.bstFromPreorder(preorder[1:i])
        
        return root
