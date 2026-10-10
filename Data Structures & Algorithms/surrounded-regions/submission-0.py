class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        rows = len(board)
        cols = len(board[0])
        queue = deque()
        for i in range(rows):
            if board[i][0] == "O":
                queue.append((i,0))
                seen.add((i,0))
            if board[i][cols-1] == "O":
                queue.append((i, cols-1))
                seen.add((i,cols-1))
        for j in range(cols):
            if board[0][j] == "O":
                queue.append((0, j))
                seen.add((0,j))
            if board[rows-1][j] == "O":
                queue.append((rows-1, j))
                seen.add((rows-1,j))
        nei = [[0,1], [1,0], [-1,0], [0,-1]]
        while queue:
            i,j = queue.popleft()
            for ni, nj in nei:
                di = ni+i
                dj = nj+j
                if 0<=di<rows and 0<=dj<cols and (di,dj) not in seen and board[di][dj] == "O":
                    seen.add((di, dj))
                    queue.append((di,dj))

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O" and (i,j) not in seen:
                    board[i][j]="X"
                    