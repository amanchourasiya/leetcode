# Similar to coin change problem with variation of initializing of second row as well
import sys
def min_coins(coins, s):
    c = len(coins)
    mint = sys.maxsize
    dp = [[0 for _ in range(s+1)] for _ in range(c+1)]
    

    # Initialize first row with INT_MAX because its not possible to form a sum with zero coins
    for col in range(s+1):
        dp[0][col] = mint
    
    # Initialize first col with 1 becasue there will always be possible to form zero sum with any no of coins

    #for row in range(c+1):
    #    dp[row][0] = 1

    # Initialize second row as well the INT_MAX for those sum that are not possibe with first value
    '''for col in range(1,s+1):
        if col % coins[0] != 0:
            dp[1][col] = 10**5
        else:
            dp[1][col] = col // coins[0]
    '''
    dp[0][0] = 0
    # Fill the rest of matrix
    for row in range(1,c+1):
        for col in range(1, s+1):
            if coins[row-1] <= col:
                dp[row][col] = min(dp[row][col-coins[row-1]] + 1, dp[row-1][col]) # Need to add on since we have included 1 coin
            else:
                dp[row][col] = dp[row-1][col]
    
    if dp[c][s] > s:
        return -1
    return dp[c][s]

print(min_coins([4,5,6], 3))

