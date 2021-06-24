def numbersInPi(pi, nums):
    cache = {}
    helper(pi, set(nums), cache)

    return cache[pi]


def helper(pi, nums, cache):
    if len(pi) == 0:
        return 0

    newNum = pi[0]
    i = 1
    while i<len(pi) and newNum not in nums:
        newNum = pi[:i+1]
        i+=1
    
    if i < len(pi):
        cache[pi] = 1 + helper(pi[i+1:], nums, cache)
    else:
        cache[pi] = 0

    return cache[pi]

pi = "3141592"
nums = ['3141', '5', '31', '2', '4159', '9', '42']
print(numbersInPi(pi, nums))
