# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res_head = ListNode(-1, head)
        group_prev = res_head
        group_start = head
        while group_start:
            group_end = self.get_tail(group_start, k)
            if not group_end:
                break
            #reverse
            group_next = group_end.next
            # print(group_prev.val, group_start.val, group_end.val)
            self.reverse_nodes(k, group_start)
            
            group_start.next = group_next
            group_prev.next = group_end

            group_prev = group_start
            group_start = group_next
        return res_head.next


    def reverse_nodes(self, k, node, prev = None):
        curr = node
        nxt = node.next
        while k and curr:
            k -= 1
            curr.next = prev
            prev = curr
            curr = nxt
            if curr:
                nxt = curr.next
        

    def get_tail(self, head, k):
        # k -= 1
        while head:
            k -= 1
            if not k:
                return head
            head = head.next
        return head
