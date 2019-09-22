#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from itertools import accumulate


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda x, y: max(y, x + y)))

