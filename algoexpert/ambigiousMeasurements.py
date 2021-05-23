def isMeasurePossible(cups, low, high, dp):
    if low < 0 and high < 0:
        return False

    if dp.get((low, high), -1) != -1:
        return dp[(low, high)]

    canMeasure = False
    for cup in cups:
        if cup[0] > low and cup[1] < high:
            canMeasure = True
            break
        if isMeasurePossible(cups, low-cup[0], high-cup[1], dp):
            canMeasure = True
            break

    dp[(low,high)] = canMeasure
    return canMeasure
        
# O(low*high*no_of_cups) | space O(low*high)

cups = [[200,210], [450,465], [800, 850]]
low = 2100
high = 2250
print(isMeasurePossible(cups, low, high,{} ))

    