class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.nei = [[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "1":
                    self.dfs(i, j)
                    res += 1
        return res

    def dfs(self, i, j):
        self.grid[i][j] = -1
        for ni, nj in self.nei:
            di, dj = ni+i, nj+j
            if 0 <= di < self.rows and 0 <= dj < self.cols and self.grid[di][dj] == "1":
                self.dfs(di, dj)
        