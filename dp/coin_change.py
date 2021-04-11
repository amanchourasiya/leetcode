def get_all(coins, s):
    c = len(coins)
    dp = [[0 for _ in range(s+1)] for _ in range(c+1)]
    for row in range(c+1):
        dp[row][0] = 1

    for row in range(1,c+1):
        for col in range(1,s+1):
            if coins[row-1] <= col:
                dp[row][col] = dp[row][col-coins[row-1]] + dp[row-1][col]
            else:
                dp[row][col] = dp[row-1][col]
    
    return dp[c][s]

print(get_all([1,2,3], 10)) 
