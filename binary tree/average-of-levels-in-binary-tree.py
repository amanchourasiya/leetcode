# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.arr = []
        self.levels(root)
        return self.arr

    def levels(self, root):
        if root is None:
            return
        
        p = []
        p.append(root)
        while(len(p) != 0):
            l = len(p)
            s = 0
            for _ in range(l):
                n = p.pop(0)
                s+=n.val
                if n.left is not None:
                    p.append(n.left)
                if n.right is not None:
                    p.append(n.right)
            self.arr.append(s/l)

