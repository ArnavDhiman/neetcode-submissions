class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.bfs(n, edges)
    def bfs(self, n, edges):
        queue = deque()
        seen = set()
        if len(edges) > n-1: return False
        adj_list = collections.defaultdict(list)
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        queue.append((0, -1))
        seen.add(0)
        while queue:
            node, parent = queue.popleft()
            for child in adj_list[node]:
                if child == parent:
                    continue
                if child in seen:
                    return False
                queue.append((child, node))
                seen.add(child)

        return len(seen) == n


    def union_find_sol(self, n, edges):
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