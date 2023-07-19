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
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        return "".join(v * k for k, v in d.items())


# @lc code=end
