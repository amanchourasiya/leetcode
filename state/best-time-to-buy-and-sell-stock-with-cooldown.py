#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

def maxProfit(prices):
    if len(prices) < 2:
        return 0

    s0 = 0
    s1 = -prices[0]
    s2 = 0

    for i in range(1, len(prices)):
        lasts2 = s2
        s2 = s1 + prices[i]
        s1 = max(s0- prices[i], s1)
        s0 = max(s0, lasts2)

    return max(s0, s2)