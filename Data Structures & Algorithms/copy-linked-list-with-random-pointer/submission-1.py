"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        return self.copy_list(head)
    def copy_list(self, head):
        node = head
        while node:
            nxt = node.next
            node.next = Node(node.val)
            node = node.next
            node.next = nxt
            node = node.next

        
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        copy_head = head.next
        node = head
        copy_node = copy_head
        while node:
            #n1 -> n2 -> n3
            #copy_n1 -> copy_n2 -> copy_n3
            
            # n1 -> copy_n1 -> n2 -> copy_n2 -> n3 -> copy_n3
            # print(node.val, copy_node.val)
            node.next = copy_node.next
            node = node.next
            if node:
                copy_node.next = node.next
                copy_node = copy_node.next
            
        return copy_head



        
    def map_list(self, head):
        h = {}
        node = head
        while node:
            h[node] = Node(node.val)
            node = node.next
        node = head
        res = h[node]
        while node:
            if node.next:
                res.next = h[node.next]
            if node.random:
                res.random = h[node.random]
            node = node.next
            res = res.next
        return h[head]
