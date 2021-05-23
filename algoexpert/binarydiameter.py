mx = 0
mn = 0
def diameter(root,curr):
    global mx, mn
    if root is None:
        return
    
    if root.left is None and root.right is None:
        if curr < mn:
            mn = curr
        elif curr > mx:
            mx = curr
        return

    diameter(root.left, curr-1)
    diameter(root.right, curr+1)


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
root.right.right.right = Node(11)
root.left.right.left = Node(10)

diameter(root,0)

print(abs(mx)+abs(mn))
    
