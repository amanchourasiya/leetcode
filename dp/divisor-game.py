# https://leetcode.com/problems/divisor-game/

class Solution:
    def divisorGame(self, N: int) -> bool:
        if N & 1 == 1:
            return False
        return True