# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2