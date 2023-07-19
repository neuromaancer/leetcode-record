#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """easy peasy

        Arguments:
            haystack {str} -- stack
            needle {str} -- pointer

        Returns:
            int -- location of the needle
        """
        return haystack.index(needle) if needle in haystack else -1

