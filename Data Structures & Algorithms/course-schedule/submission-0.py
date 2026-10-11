class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inorder = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)
        for i in range(numCourses):
            inorder[i] = 0
            adj_list[i] = []
        for p1, p2 in prerequisites:
            inorder[p1] += 1
            adj_list[p2].append(p1)

        queue = deque()
        taken = 0
        for k,v in inorder.items():
            if not v:
                queue.append(k)
                # taken += 1

        while queue:
            k = queue.popleft()
            taken += 1
            for child in adj_list[k]:
                inorder[child] -= 1
                if not inorder[child]:
                    queue.append(child)
                    
        return taken == numCourses