def branchsum(root, res, currsum):
    if root is None:
        return

    if root.left is None and root.right is None:
        res.append(currsum+root.val)
        return

    branchsum(root.left, res, currsum+ root.val)
    branchsum(root.right, res, currsum+root.val)


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
root.left.right.left = Node(10)

res = []

branchsum(root, res, 0)
print(res)

    
    
