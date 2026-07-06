# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)

        dummy_head.next = head

        curr = dummy_head.next

        while curr and curr.next:
            a = curr.val
            b = curr.next.val

            curr.val = b
            curr.next.val = a

            curr = curr.next.next
        
        return dummy_head.next