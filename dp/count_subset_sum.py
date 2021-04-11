def subset_sum_count(arr, s):
    dp = [[0 for _ in range(s+1)] for _ in range(len(arr)+1)]

    for row in range(len(arr)+1):
        dp[row][0] = 1
    print(dp)
    for row in range(1,len(arr)+1):
        for col in range(1, s+1):
            if arr[row-1] <= col:
                dp[row][col] = dp[row-1][col-arr[row-1]] + dp[row-1][col]
            else:
                dp[row][col] = dp[row-1][col]
            
    print(dp)
    return dp[len(arr)][s]

is_sum_present = subset_sum_count([2,3,5,6,8,10],10) 
print(is_sum_present)