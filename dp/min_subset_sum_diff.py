# https://leetcode.com/problems/last-stone-weight-ii/

def min_subset_sum_diff(arr):
    s = sum(arr)
    r = s
    s = s // 2
    
    l = len(arr)
    dp = [[False for _ in range(s+1)] for _ in range(l+1)]
    for row in range(l+1):
        dp[row][0] = True
    
    for row in range(1,l+1):
        for col in range(1,s+1):
            if arr[row-1] <= col:
                dp[row][col] = (dp[row-1][col-arr[row-1]]) or (dp[row-1][col])
            else:
                dp[row][col] = dp[row-1][col]

    
    m = 0
    
    for v in range(s, -1, -1):
        if dp[l][v] == True:
            m = r - (2 * v)
            break
    return m


res = min_subset_sum_diff([31,26,33,21,40])
print(res) 