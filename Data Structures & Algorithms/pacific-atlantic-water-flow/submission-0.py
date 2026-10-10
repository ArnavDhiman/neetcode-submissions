class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])
        self.heights = heights
        p_queue = deque()
        a_queue = deque()
        for i in range(self.rows):
            p_queue.append((i,0))
            a_queue.append((i,self.cols-1))
        for j in range(self.cols):
            p_queue.append((0, j))
            a_queue.append((self.rows-1, j))

        pacific = self.bfs(p_queue)
        atlantic = self.bfs(a_queue)

        # print(pacific)
        # print(atlantic)
        res = []
        for i in range(self.rows):
            for j in range(self.cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res

    def bfs(self, queue):
        ocean = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for i, j in queue:
            ocean[i][j] = True
        nei = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue:
            i, j = queue.popleft()
            for ni, nj in nei:
                di, dj = ni+i, nj+j
                if 0<=di<self.rows and 0<=dj<self.cols and not ocean[di][dj] and self.heights[i][j] <= self.heights[di][dj]:
                    ocean[di][dj] = True
                    queue.append((di, dj))
        return ocean
