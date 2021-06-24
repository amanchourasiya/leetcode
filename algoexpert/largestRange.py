# Space O(n) | time O(n) for dp 

def largestRange(arr):
    low = 0
    high = 0
    
    dp = {}
    for value in arr:
        dp[value] = False
    
    for value in arr:
        if dp[value]:
            continue
        
        # search for smaller values
        dp[value] = True
        currentLow = value
        while currentLow in dp:
            dp[currentLow] = True
            currentLow-=1

        currentMax = value
        while currentMax in dp:
            dp[currentMax] = True
            currentMax+=1

        currentLow+=1
        currentMax-=1
        if currentMax-currentLow > high-low:
            low = currentLow
            high = currentMax


    return [low, high]

arr = [11,3,0,15,10,7,12,6]
print(largestRange(arr))

