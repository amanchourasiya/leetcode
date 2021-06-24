def maxSumIncreasingSubsequence(arr): # time O(n^2) | space O(n)
    l = len(arr)
    newarr = [0 for _ in range(l)]

    newarr[0] = arr[0]
    for curr in range(1, l):
        for j in range(curr):
            if arr[j] < arr[curr] and newarr[curr] < arr[curr] + newarr[j]:
                newarr[curr] = arr[curr]+ newarr[j]

    return max(newarr)

arr = [8,12,2,3,15,5,7]
print(maxSumIncreasingSubsequence(arr))