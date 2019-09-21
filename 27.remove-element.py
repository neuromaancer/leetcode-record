#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """the key to solve the problem is to be familiar with in-place loop: while and func: remove

        Arguments:
            nums {List[int]} -- list to processed
            val {int} -- value

        Returns:
            int -- length of the list
        """
        while val in nums:
            nums.remove(val)

