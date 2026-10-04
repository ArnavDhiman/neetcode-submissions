class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)

        while len(pq) > 1:
            n1, n2 = heapq.heappop(pq), heapq.heappop(pq)
            # print(n1, n2, n1-n2)
            n1 -= n2
            if n1 != 0:
                if n1 > 0:
                    n1 *= -1
                heapq.heappush(pq, n1)
        return -pq[0] if pq else 0
        