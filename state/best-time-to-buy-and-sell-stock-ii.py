# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/



def max_profit(prices):
    if len(prices) < 2:
        return 0
    p = 0
    b = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            p += prices[i] - prices[i-1]

    return p

print(max_profit([7,1,5,3,6,4]))