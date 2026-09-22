# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        list1 = []
        curr = head

        while curr:
            list1.append(curr.val)
            curr = curr.next

        return list1 == list1[::-1]