# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0:
            return False
        s = s // 2
        
        dp = [[False for _ in range(s+1)] for _ in range(len(nums)+1)]

        for row in range(len(nums)+1):
            dp[row][0] = True

        for row in range(1,len(nums)+1):
            for col in range(1, s+1):
                if nums[row-1] <= col:
                    dp[row][col] = dp[row-1][col-nums[row-1]] or dp[row-1][col]
                else:
                    dp[row][col] = dp[row-1][col]
        #print(dp)
        return dp[len(nums)][s]

is_partition_present = Solution().canPartition([1,7,7,11])
print(is_partition_present)