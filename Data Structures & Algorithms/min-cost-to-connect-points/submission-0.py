class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        self.parent = [-1 for _ in range(l)]
        set_left = l
        heap = []
        for i in range(l):
            for j in range(i+1, l):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(heap, (dist, i, j))
        # print("HEAP --- ",heap)
        total = 0
        while heap:
            dist, p1, p2 = heapq.heappop(heap)
            if self.union(p1, p2):
                set_left -= 1
                total += dist
                # print("TOTAL and SET LEFT --- ",total, set_left)
                # print("JOINING POINTS -- ", points[p1], " AND ",points[p2])
            if set_left == 1:
                break
        return total

    def union(self, p1, p2):
        parent1 = self.find(p1)
        parent2 = self.find(p2)
        if parent1 == parent2:
            return False
        if self.parent[parent1] > self.parent[parent2]:
            self.parent[parent2] += self.parent[parent1]
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] += self.parent[parent2]
            self.parent[parent2] = parent1
        # print("PARENT --- ",self.parent)
        return True
        
    def find(self, p):
        while self.parent[p] >= 0:
            p = self.parent[p]
        return p