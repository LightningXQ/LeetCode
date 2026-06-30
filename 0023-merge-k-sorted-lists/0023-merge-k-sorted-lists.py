# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not any(lists): return None

        result = list()

        for lst in lists:
            while lst:
                result.append(lst.val)
                lst = lst.next

        result.sort()

        head = ListNode()
        head.val = result[0]
        current = head
        
        for e in result[1:]:
            current.next = ListNode()
            current = current.next
            current.val = e
            
        return head
