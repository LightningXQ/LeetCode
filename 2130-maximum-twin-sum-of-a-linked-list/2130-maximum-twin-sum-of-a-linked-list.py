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
        mx = 2
        while slow:
            tmp = lst[pivot] + slow.val
            mx = mx if mx > tmp else tmp
            pivot -= 1
            slow = slow.next

        return mx
