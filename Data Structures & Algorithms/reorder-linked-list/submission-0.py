# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        n1 = head
        n2 = slow
        if fast:
            n2 = slow.next
        curr = n2
        prev = None
        nxt = n2.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if curr:
                nxt = curr.next
        n2 = prev
        node = n1
        n1 = n1.next
        flag = 1
        while n1 and n2:
            # print(n1.val, n2.val, node.val)
            if flag > 0:
                node.next = n2
                n2 = n2.next
            else:
                node.next = n1
                n1 = n1.next
            node = node.next
            flag *= -1
        # print(n1.val, n2.val, prev.val)
        return None