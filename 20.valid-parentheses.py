#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in dic:
                stack.append(dic.get(char))
            elif not stack or stack.pop() != char:
                return False
        return not stack

