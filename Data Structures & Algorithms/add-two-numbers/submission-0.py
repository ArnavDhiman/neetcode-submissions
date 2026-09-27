# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode(0)
        res_node = res_head
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            l1, l2 = l1.next, l2.next
            if s > 9: c,s = 1, s-10
            else: c = 0
            res_node.next = ListNode(s)
            res_node = res_node.next
        while l1:
            s = l1.val + c
            l1 = l1.next
            if s > 9: c,s = 1, s-10
            else: c = 0
            res_node.next = ListNode(s)
            res_node = res_node.next
        while l2:
            s = l2.val + c
            l2 = l2.next
            if s > 9: c,s = 1, s-10
            else: c = 0
            res_node.next = ListNode(s)
            res_node = res_node.next
        if c: 
            res_node.next = ListNode(c)
        return res_head.next