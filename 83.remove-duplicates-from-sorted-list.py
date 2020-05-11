#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:  # until the end
            while (
                cur.next and cur.next.val == cur.val
            ):  # if has the duplication on next val
                cur.next = (
                    cur.next.next
                )  # skip the duplication or reconnect the node list
            cur = cur.next  # pointer moves
        return head  # return the whole node list


# @lc code=end
