#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, idx + 1]
            dic[num] = idx

# @lc code=end
