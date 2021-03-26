# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        i = 0
        j = 0
        while j < n:
            if i >= m:
                break

            if s[i] == t[j]:
                i+=1
            j+=1
        if i >= m:
            return True
        return False
