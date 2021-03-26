# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices) :
        # Kadane algorithm
        maxpro = 0
        minprice = 10 ** 5
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            maxpro = max(maxpro, prices[i] - minprice)
        
        
        return maxpro

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
