# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not any(lists): return None

        n = len(lists)
        done = [False] * n
        result = list()

        while True:
            min_val = 10 ** 4 + 1
            min_val_idx = 10 ** 4

            for i in range(n):
                if not lists[i]: continue
                if min_val > lists[i].val:
                    min_val = lists[i].val
                    min_val_idx = i

            if min_val == 10 ** 4 + 1: break
            result.append(min_val)

            lists[min_val_idx] = lists[min_val_idx].next

        head = ListNode()
        head.val = result[0]
        current = head
        
        for e in result[1:]:
            current.next = ListNode()
            current = current.next
            current.val = e
            
        return head

