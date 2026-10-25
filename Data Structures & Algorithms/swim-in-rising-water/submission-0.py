class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # max(grid[i][j], step), step, i, j
        heap = [(grid[0][0],0,0,0)]
        n = len(grid)
        MAX_VAL = (n*n)+1
        nei = [[1,0],[0,1],[-1,0],[0,-1]]
        
        while heap:
            res, step, i, j = heapq.heappop(heap)
            # print(step, i, j, res)
            if grid[i][j] != MAX_VAL:
                grid[i][j] = MAX_VAL
                if i == n-1 and j == n-1:
                    # print(res, step, n)
                    # print(grid)
                    return res
                for ni, nj in nei:
                    di, dj = i+ni, j+nj
                    if 0<=di<n and 0<=dj<n and grid[di][dj] != MAX_VAL:
                        # print("ADDING POINTS -- ", di, dj, grid[di][dj])
                        heapq.heappush(heap, (max(res, step+1, grid[di][dj]), step+1, di, dj))
        return -1