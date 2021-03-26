# https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for r in range(m):
            for c in range(n):
                if c == 0:
                    dp[r][c] = mat[r][c]
                else:
                    dp[r][c] = dp[r][c-1] + mat[r][c]
        
        for c in range(n):
            for r in range(m):
                if r == 0:
                    dp[r][c] = dp[r][c]
                else:
                    dp[r][c] = dp[r][c]+ dp[r-1][c]
        
        
        ans = [[0 for i in range(n)] for j in range(m)]
        for r in range(m):
            for c in range(n):
                r2 = r + K
                c2 = c + K
                r1 = r -K
                c1 = c -K
                if r+K >= m:
                    r2 = m-1
                if c+K >= n:
                    c2 = n-1
                if r-K < 0:
                    r1 = 0
                if c-K < 0:
                    c1 = 0
                
                s = dp[r2][c2]
                # Delete all extra values collected
                count = 0

                if r1 != 0:
                    s = s - dp[r1-1][c2]
                    count+=1
                if c1 != 0:
                        s = s - dp[r2][c1-1]
                        count+=1
                if count == 2:
                    s = s + dp[r1-1][c1-1]
                ans[r][c] = s
        return ans
