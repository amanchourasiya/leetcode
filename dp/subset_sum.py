def subset_sum(arr, s):
    dp = [[False for _ in range(s+1)] for _ in range(len(arr)+1)]

    for row in range(len(arr)+1):
        dp[row][0] = True

    for row in range(1,len(arr)+1):
        for col in range(1,s+1):
            if arr[row-1] <= s:
                dp[row][col] = dp[row-1][col-arr[row-1]] or dp[row-1][col]
            else:
                dp[row][col] = dp[row-1][col]
    print(dp)
    return dp[len(arr)][s]

is_sum_present = subset_sum([2,3,7,8,10], 5) 
print(is_sum_present)