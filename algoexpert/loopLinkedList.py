def findStartOfLoop(head):
    if head is None:
        return None

    if head.next is None or head.next.next is None:
        return None
    fastPtr = head.next.next
    slowPtr = head.next

    found = False

    while fastPtr is not None and fastPtr.next is not None:
        if fastPtr == slowPtr:
            found = True
            break

        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

    if not found:
        return None
    
    slowPtr = head
    while slowPtr != fastPtr:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next

    return slowPtr

