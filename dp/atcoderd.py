def maxProfit(values, weights, capacity, n):
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for row in range(1, n+1):
        for col in range(1, capacity+1):
            if weights[row-1] <= col:
                dp[row][col] = max(dp[row-1][col] , dp[row-1][col-weights[row-1]] + values[row-1])
            else:
                dp[row][col] = dp[row-1][col]
    print(dp)
    return dp[-1][-1]


n = 3
capacity = 8
values = [30,50,60]
weights = [3,4,5]
print(maxProfit(values, weights, capacity, n))


                