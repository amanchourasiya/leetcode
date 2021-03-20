# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.arr = []
        self.level(root)
        return self.arr

    def level(self,root):
        if root is None:
            return

        self.p = []
        self.p.append(root)
        while len(self.p) != 0:
            a = []
            for _ in range(len(self.p)):
                n = self.p.pop(0)
                a.append(n.val)
                if n.left is not None:
                    self.p.append(n.left)
                if n.right is not None:
                    self.p.append(n.right)
            self.arr.append(a)


