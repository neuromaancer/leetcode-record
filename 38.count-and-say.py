#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        """diffcult to understand the problem, use the basic method

        Arguments:
            n {int} -- input num

        Returns:
            str -- count and say string output
        """
        result = "1"
        for i in range(n - 1):
            count = 1
            temp = list()
            for idx in range(1, len(result)):
                if result[idx] == result[idx - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(result[idx - 1])
                    count = 1
            temp.append(str(count))
            temp.append(result[-1])
            result = "".join(temp)
        return result

