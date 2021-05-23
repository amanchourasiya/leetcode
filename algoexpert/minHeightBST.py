def minBst(arr, left, right):
    if left > right:
        return None
    mid = (left + right) /2
    root = Node(arr[mid])
    root.left = minBst(arr, left, mid-1)
    root.right = minBst(arr, mid+1, right)

    return root