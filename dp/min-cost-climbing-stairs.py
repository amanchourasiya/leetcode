class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = cost[0]
        second = cost[1]
        if n < 2:
            return min(first, second)
        
        for i in range(2, n):
            cur = cost[i] + min(first, second)
            first = second
            second = cur

        return min(first, second)

    ''' recursive
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = [-1 for i in range(len(cost))]
        self.solve(cost, 0)
        return min(self.dp[0], self.dp[1])

    def solve(self, cost, index):
        if index > len(cost)-1:
            return 0
        
        if self.dp[index] != -1:
            return self.dp[index]
        
        self.dp[index] =  cost[index] + min(self.solve(cost, index+1), self.solve(cost, index+2))
        return self.dp[index]
    '''
            
        
