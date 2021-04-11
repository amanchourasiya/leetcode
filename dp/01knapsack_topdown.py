def knapsack(values, weights, capacity, size):
    dp = [[0 for _ in range(capacity+1)] for _ in range(size+1)]
    for row in range(len(dp)):
        dp[row][0] = 0

    for col in range(len(dp[0])):
        dp[0][col] = 0
    
    for row in range(1,size+1):
        for col in range(1,capacity+1):
            if weights[row-1] <= col:
                dp[row][col] = max(values[row-1] + dp[row-1][col-weights[row-1]], dp[row-1][col])
            else:
                dp[row][col] = dp[row-1][col]
    print(dp)
    return dp[size][capacity]

max_profit = knapsack([60, 100, 120],[10, 20, 30,],50, 3)
print(max_profit)
