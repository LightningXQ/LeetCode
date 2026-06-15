# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head: return None

        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        m = n // 2
        curr = head
        dummy_head = ListNode()
        tail = dummy_head

        for i in range(n):
            if i == m:
                curr = curr.next
                continue
            tail.next = ListNode(curr.val, None)
            curr = curr.next
            tail = tail.next

        return dummy_head.next
