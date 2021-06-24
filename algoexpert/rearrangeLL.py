class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert(head, node):
    tmp = head

    while tmp.next is not None:
        tmp = tmp.next

    tmp.next = node

def rearrange(head, val):
    left = None
    centre = None
    right = None

    tmp = head
    while tmp is not None:
        print(tmp.val)
        if tmp.val < val:
            if left is None:
                left = tmp
            else:
                insert(left, tmp)
        elif tmp.val > val:
            if right is None:
                right = tmp
            else:
                insert(right, tmp)
        else:
            if centre is None:
                centre = tmp
            else:
                insert(centre, tmp)
        prevTmp = tmp
        tmp = tmp.next
        prevTmp.next = None

        

    insert(centre, right)
    insert(left, centre)
    return left

def printll(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end=' ')
        tmp = tmp.next
    print()
# 3 0 5 2 1 4

head = Node(3)
insert(head, Node(0)) 
insert(head, Node(5))
insert(head, Node(2))
insert(head, Node(1))
insert(head, Node(4))

printll(head)
newHead = rearrange(head, 3)
printll(newHead)



