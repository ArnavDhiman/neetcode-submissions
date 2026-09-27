# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(-1, head)
        node = head
        while n:
            node = node.next
            n -= 1
        slow = prev
        while node:
            slow = slow.next
            node = node.next
        # print(slow.val)
        slow.next = slow.next.next
        return prev.next