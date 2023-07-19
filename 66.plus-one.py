#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])

        return digits

