# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        dp = [0] * (N+1) 

        for i in range(1, N+1):
            curmax = 0
            for j in range(1, min(k,i) + 1):
                
                curmax = max(curmax, arr[i-j] )
                dp[i] = max(dp[i], dp[i-j] + curmax *j)
            
            
        return dp[N]
