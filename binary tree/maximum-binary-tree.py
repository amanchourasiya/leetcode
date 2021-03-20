# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        st = []
        for i in range(len(nums)):
            node = TreeNode(nums[i])
            while (len(st) != 0 and st[-1].val < nums[i]):
                node.left = st[-1]
                st.pop(-1)
            if len(st) != 0 :
                st[-1].right = node
            st.append(node)
            
        return st[0]
