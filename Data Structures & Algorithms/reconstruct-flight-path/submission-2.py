class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        return self.Hierholzer(tickets)
    def Hierholzer(self, tickets):
        adj_list = collections.defaultdict(list)
        tickets.sort(reverse = True)
        for source, dest in tickets:
            adj_list[source].append(dest)
        stack = ["JFK"]
        path = []
        while stack:
            node = stack[-1]
            if adj_list[node]:
                stack.append(adj_list[node].pop())
            else:
                path.append(stack.pop())
        return path[::-1]

    def backtrack(self, tickets):
        adj_list = collections.defaultdict(list)
        incoming = collections.defaultdict(int)
        tickets.sort()
        
        for source, dest in tickets:
            adj_list[source].append(dest)
            incoming[(source, dest)] += 1
        
        res = ["JFK"]
        def dfs(source):
            if len(res) == len(tickets)+1:                
                return True
                
            for dest in adj_list[source]:
                if incoming[(source, dest)] > 0:
                    incoming[(source, dest)] -= 1
                    res.append(dest)
                    if dfs(dest):
                        return True
                    incoming[(source, dest)] += 1
                    res.pop()
            return False
        dfs("JFK")
        return res