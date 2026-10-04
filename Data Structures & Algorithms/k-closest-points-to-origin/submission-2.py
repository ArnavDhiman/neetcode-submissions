class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-self.get_dist(x, y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res


    def get_dist(self, x, y):
        return math.sqrt(x**2+y**2)