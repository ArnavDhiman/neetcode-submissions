class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj_list = {}
        inorder = {}
        queue = deque()
        for i in range(numCourses):
            adj_list[i] = []
            inorder[i] = 0

        for p1, p2 in prerequisites:
            inorder[p1] += 1
            adj_list[p2].append(p1)

        for k, v in inorder.items():
            if not v:
                queue.append(k)
        
        while queue:
            k = queue.popleft()
            res.append(k)

            for c in adj_list[k]:
                inorder[c] -= 1
                if not inorder[c]:
                    queue.append(c)
        # print(res)
        return [] if len(res) != numCourses else res