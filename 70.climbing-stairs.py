#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = {0: 1, 1: 1, 2: 1}
        i = 2
        while i < n + 1:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n]

# @lc code=end
