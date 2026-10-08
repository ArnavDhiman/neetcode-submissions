class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = res = 0
        nei = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1
        while queue:
            i, j, time = queue.popleft()
            res = max(res, time)
            for ni, nj in nei:
                di = i+ni
                dj = j+nj
                if 0<=di<rows and 0<=dj<cols and grid[di][dj] == 1:
                    grid[di][dj] = 2
                    queue.append((di,dj,time+1))
                    fresh -= 1
        return res if fresh == 0 else -1