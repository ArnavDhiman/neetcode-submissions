"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        queue = deque()
        if node:
            queue.append(node)
            hmap[node] = Node(node.val)
        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in hmap:
                    queue.append(nei)
                    hmap[nei] = Node(nei.val)
        # print(hmap)
        for orig, copy in hmap.items():
            for nei in orig.neighbors:
                copy.neighbors.append(hmap[nei])
        return hmap[node] if node else None