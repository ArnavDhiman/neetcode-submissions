class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = None
        self.tail = None
        self.create_pos_list()
        self.cap = capacity

    def get(self, key: int) -> int:
        res = -1
        if key in self.cache:
            self.move_to_head(self.cache[key])
            res = self.cache[key].val
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
        else:
            node = ListNode(key, value)
            self.cache[key] = node

        self.move_to_head(self.cache[key])

        if len(self.cache.keys()) > self.cap:
            key = self.pop_from_tail()
            del(self.cache[key])
        
    def pop_from_tail(self):
        node = self.tail.prev
        prev = node.prev
        prev.next = self.tail
        self.tail.prev = prev
        return node.key

    def move_to_head(self, node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        nxt = self.head.next        
        self.head.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = self.head
        

    def create_pos_list(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
