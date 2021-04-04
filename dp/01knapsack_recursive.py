
def knapsack(values, weights, capacity, size):
    if capacity == 0 or size == 0:
        return 0
    
    if weights[size-1] <= capacity:
        return max(values[size-1] + knapsack(values, weights, capacity-weights[size-1], size-1), knapsack(values, weights, capacity, size-1))
    else:
        return knapsack(values, weights, capacity, size-1)


max_profit = knapsack([60, 100, 120],[10, 20, 30,],50, 3)
print(max_profit)