def isMonotonic(arr):
    # check with first and last element
    if arr[0] == arr[-1]:
        # then all elements should be same
        element = arr[0]
        for num in arr:
            if num != element:
                return False
    elif arr[0] < arr[-1]:
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
    else:
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                return False
    return True

