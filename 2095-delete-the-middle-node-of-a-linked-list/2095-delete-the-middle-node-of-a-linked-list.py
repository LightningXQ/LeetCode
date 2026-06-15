# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next: return None

        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        m = n // 2
        curr = head

        curr = head
        for i in range(m - 1):
            curr = curr.next
        curr.next = curr.next.next

        return head
