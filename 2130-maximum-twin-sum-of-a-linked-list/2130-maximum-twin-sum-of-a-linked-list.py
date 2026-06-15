# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        lst = list()
        while head:
            lst.append(head.val)
            head = head.next

        n = len(lst)
        mx = 2

        for i in range(n):
            if i > n // 2: break
            val = lst[i] + lst[n - i - 1]
            mx = max(mx, val)

        return mx