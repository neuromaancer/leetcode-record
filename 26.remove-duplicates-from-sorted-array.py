#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ the difficulty is to change the list in place, if not "return len(set(nums))"

        Arguments:
            nums {List[int]} -- list to treated

        Returns:
            int -- the length of nums
        """
        if not nums:
            return 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j + 1] = nums[j + 1], nums[i]
                j = j + 1
        return j + 1
