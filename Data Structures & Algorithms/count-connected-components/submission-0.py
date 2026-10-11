class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = [-1 for _ in range(n)]
        for e1, e2 in edges:
            self.union(e1, e2)
        c = 0
        for p in self.parents:
            if p < 0:
                c+=1
        return c

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 != parent2:
            if self.parents[parent1] > self.parents[parent2]:
                self.parents[parent2] += self.parents[parent1]
                self.parents[parent1] = parent2
            else:
                self.parents[parent1] += self.parents[parent2]
                self.parents[parent2] = parent1
        
    def find(self, node):
        while self.parents[node] >= 0:
            node = self.parents[node]
        return node

