import copy

def findPermutations(arr):
    perms = []

    helper(arr, 0, perms, len(arr))
    return perms

def helper(arr, i, perms, l):
    if i >= l-1:
        perms.append(copy.deepcopy(arr)) # O(n n!)
    else:
        for j in range(i, l):
            arr[i],arr[j] = arr[j],arr[i]
            helper(arr, i+1, perms, l)          # O(n)
            arr[i], arr[j] = arr[j], arr[i]

print(findPermutations([1,2,3]))

# space O(n!n)| time O(n! n)