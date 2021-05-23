class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        return traverse(root)
        
import copy

def traverse(root):
    print('traverse')
    if root is None:
        print('empty')
        return []
    queue = []
    stack = []
    res = []
    reverse = False

    queue.append(root)
    
    while (len(queue)> 0):
        print('queue', queue)
        res1 = []
        level = len(queue)
        while level >0:
            print('level', level)
            level-=1
            node = queue.pop(0)
            print(node.val)
            if node is None:
                continue
            if reverse:
                stack.append(node.val)
            else:
                res1.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            
        
        if reverse:
             while len(stack) !=0:
                  res1.append(stack.pop(-1))
             reverse = False
        else:
               reverse = True
        res.append(copy.deepcopy(res1))
   
    return res

def test():
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    print(traverse(t))

test()
