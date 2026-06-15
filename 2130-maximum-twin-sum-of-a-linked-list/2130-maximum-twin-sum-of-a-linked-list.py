# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow = head
        fast = head
        lst = list()

        while fast:
            lst.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        pivot = -1
        while slow:
            lst[pivot] += slow.val
            pivot -= 1
            slow = slow.next

        return max(lst)