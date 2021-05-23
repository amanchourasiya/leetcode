def nodedepth(root, currdepth):
    if root is None:
        return currdepth - 1

    if root.left is None and root.right is None:
        return currdepth

    return currdepth + nodedepth(root.left, currdepth+1) + nodedepth(root.right, currdepth+1)


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

print(nodedepth(root, 0))
