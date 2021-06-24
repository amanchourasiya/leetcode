def minRewards(arr):
    l = len(arr)
    res = [1 for _ in range(l)]
    # do a pass forward
    for i in range(l):
        if arr[i] >= arr[i-1]:
            res[i] = res[i-1]+1

    # do a pass backward
    for i in range(l-2, -1,-1):
        if arr[i] > arr[i+1]:
            res[i] = max(res[i], 1+res[i+1])

    return sum(res)

arr = [8,4,2,1,3,6,7,9,5]
print(minRewards(arr))