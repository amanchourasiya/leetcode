# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create dp table and fill first row and column
        R = len(text1)
        C = len(text2)
        dp = [[0 for _ in range(C+1)] for _ in range(R+1)]
        for row in range(R+1):
            dp[row][0] = 0

        for col in range(1,C+1):
            dp[0][col] = 0

        for row in range(1,R+1):
            for col in range(1,C+1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])

        return ''.join(self.traceback(dp,R,C, text1,text2)[::-1]) 

        
    def traceback(self, dp, R, C, text1, test2):
        val = dp[R][C]
        res = []
        while(val != 0):
            if val == dp[R][C-1]:
                C-=1
            elif val == dp[R-1][C]:
                R-=1
            else:
                R-=1
                C-=1
                val = dp[R][C]
                res.append(text1[R])
        return res

def run():
    s = Solution()
    print(s.longestCommonSubsequence('abcde', 'ace'))

run()