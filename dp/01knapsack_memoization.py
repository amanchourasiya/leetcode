
def knapsack(values, weights, capacity, size):
    global dp
    if capacity == 0 or size == 0:
        return 0
    if dp[size][capacity] != -1:
        return dp[size-1][capacity]


    if weights[size-1] <= capacity:
        dp[size][capacity] = max(values[size-1] + knapsack(values, weights, capacity-weights[size-1], size-1), knapsack(values, weights, capacity, size-1))
        return dp[size][capacity]
    else:
        dp[size][capacity] = knapsack(values, weights, capacity, size-1)
        return dp[size][capacity]


dp = [[-1 for _ in range(50+1)] for _ in range(3+1)]
max_profit = knapsack([60, 100, 120],[10, 20, 30,],50, 3)
print(max_profit)