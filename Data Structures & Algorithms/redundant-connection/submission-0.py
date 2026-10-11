class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parents = [-1 for _ in range(len(edges)+1)]
        for edge in edges:
            t = self.union(edge)
            if t:
                return t
        return []
    def union(self, edge):
        p1 = self.find(edge[0])
        p2 = self.find(edge[1])

        if p1 == p2:
            return edge
        else:
            if self.parents[p1] > self.parents[p2]:
                self.parents[p2] += self.parents[p1]
                self.parents[p1] = p2
            else:
                self.parents[p1] += self.parents[p2]
                self.parents[p2] = p1
        return None
    def find(self, node):
        while self.parents[node] >= 0:
            node = self.parents[node]
        return node