#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
import bisect
class Solution:
    """one line solution with bisect package
    bisect: https://docs.python.org/3.7/library/bisect.html
    basic binary search by hand:

    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

    Returns:
        int -- position of the target
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

