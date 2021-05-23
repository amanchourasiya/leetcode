def nodedepth(root):
    stack = []
    sm = 0
    stack.append((root, 0))
    while len(stack) > 0:
        ele = stack.pop(-1)
        sm = sm + ele[1]
        if ele[0].left is not None:
            stack.append((ele[0].left, ele[1]+1))

        if ele[0].right is not None:
            stack.append((ele[0].right, ele[1]+1))

    return sm

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

print(nodedepth(root))