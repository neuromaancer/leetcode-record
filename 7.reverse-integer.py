#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(-x)[::-1])
        return x if -(2 ** 31) < x < (2 ** 31) - 1 else 0

