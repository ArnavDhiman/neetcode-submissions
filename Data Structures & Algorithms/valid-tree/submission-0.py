class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.parents = [-1 for _ in range(n)]
        for e1, e2 in edges:
            if not self.union(e1, e2):
                return False
        c = 0
        for p1 in self.parents:
            if p1 < 0:
                c += 1
        return c == 1

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return False
        if parent1 != parent2:
            if self.parents[parent1] > self.parents[parent2]:
                self.parents[parent2] += self.parents[parent1]
                self.parents[parent1] = parent2
            else:
                self.parents[parent1] += self.parents[parent2]
                self.parents[parent2] = parent1
        # print(self.parents, node1, node2)
        return True
        
    def find(self, node):
        while self.parents[node] >= 0:
            node = self.parents[node]
        return node