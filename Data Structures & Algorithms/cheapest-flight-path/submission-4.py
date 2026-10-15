class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq = []
        adj = {}
        seen = {}
        for frm, to, price in flights:
            if frm not in adj:
                adj[frm] = []
            adj[frm].append((to, price))
        pq.append((0, 0, src))
        while pq:
            price, stops, to = heapq.heappop(pq)
            # print(price, stops, to)
            seen[to] = stops
            if to == dst:
                return price
            if stops <= k and to in adj:
                for c, p in adj[to]:
                    if (c not in seen) or (c in seen and seen[c] > stops):
                        heapq.heappush(pq, (price+p, stops+1, c))
        return -1