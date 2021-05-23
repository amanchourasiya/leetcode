def powerset(arr):
    res = [[]]

    for i in arr:
        l = len(res)
        for tmparr in range(l):
            res.append(res[tmparr]+[i])

    return res

print(powerset([1,2,3]))

# space O(2^n * n) | time O(2^n * n)