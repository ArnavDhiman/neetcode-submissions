class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j, 1))
        nei = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue:
            # print(queue)
            i, j, step = queue.popleft()
            for ni, nj in nei:
                di = ni+i
                dj = nj+j
                if 0<=di<rows and 0<=dj<cols and grid[di][dj]>step:
                    grid[di][dj] = step
                    queue.append((di,dj,step+1))
                    # print(di, dj, step)
                    
        
