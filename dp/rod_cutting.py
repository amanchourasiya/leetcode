# Its a variation of unbounded kanpsack where we can take one element multiple times

def max_profit(l, p, rod):
    dp = [[0 for _ in range(rod+1)] for _ in range(len(l)+1)]

    for row in range(1,len(l)+1):
        for col in range(1,rod+1):
            if l[row-1] <= col:
                dp[row][col] = max(p[row-1]+dp[row][col - l[row-1]], dp[row-1][col])
            else:
                dp[row][col] = dp[row-1][col]
            
    return dp[len(l)][rod]

print(max_profit([1,2,3,4,5,6,7,8], [3,5,8,9,10,17,17,20], 8))