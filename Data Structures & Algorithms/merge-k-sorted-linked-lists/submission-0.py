# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        res = ListNode()
        node = res
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val,i, l))
        while h:
            n,i,l = heapq.heappop(h)
            node.next = l
            
            node = node.next
            l = l.next
            
            if l:
                heapq.heappush(h, (l.val,i, l))
        return res.next