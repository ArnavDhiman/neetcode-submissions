class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        seen = set()
        hq = []
        
        for u,v,t in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((v,t))
        # seen.add(k)
        # print(adj)
        hq.append((0,k))
        while hq:
            # print(seen, hq)
            curr_t, v = heapq.heappop(hq)
            if v in seen:
                continue
            seen.add(v)
            
            if len(seen) == n:
                return curr_t
            if v in adj:
                for child in adj[v]:
                    if child[0] not in seen:
                        heapq.heappush(hq, (child[1]+curr_t, child[0]))
        return -1