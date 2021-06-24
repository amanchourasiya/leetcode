def flattenBinaryTree(root):
    return flattenTree(root)[0]

def flattenTree(node):
    if node.left is None:
        leftMostNode = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connect(leftSubtreeRightMost, node)
        leftMostNode = leftSubtreeLeftMost

    if root.right is None:
        rightMostNode = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connect(node, rightSubtreeLeftMost)
        rightMostNode = rightSubtreeRightMost

    return [leftMostNode, rightMostNode]

def connect(left, right):
    left.right = right
    right.left = left

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(7)

flattenBinaryTree(root)
print(root.val,root.right.val, root.right.right.val)
