#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict(Counter(s))
        s_sorted = ""
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        for k, v in d.items():
            s_sorted += v * k
        return s_sorted


# @lc code=end
