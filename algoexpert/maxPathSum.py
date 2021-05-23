# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return None
        
        self.maxSum  = root.val
        self.findMaxPathSum(root)
        return self.maxSum
        
    def findMaxPathSum(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            if self.maxSum < root.val:
                self.maxSum = root.val
            return root.val


        leftsum = self.findMaxPathSum(root.left)
        rightsum = self.findMaxPathSum(root.right)

        tmp = max(root.val+leftsum, root.val)
        tmp2 = max(root.val+rightsum, root.val)

        self.maxSum = max(self.maxSum, tmp+tmp2-root.val)
        return max(tmp, tmp2)
