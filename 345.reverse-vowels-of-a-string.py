#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vows = set("aoieuAOIEU")
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] not in vows:
                l += 1
                continue
            if s[r] not in vows:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)


# @lc code=end
