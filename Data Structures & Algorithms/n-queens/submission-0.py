class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()
        all_queen = []
        def recur(i, r, q):
            if i == 0:
                all_queen.append(q[:])
                return
            for c in range(n):
                if c not in cols and c+r not in diag1 and r-c not in diag2:
                    cols.add(c)
                    diag1.add(r+c)
                    diag2.add(r-c)
                    q.append(c)
                    recur(i-1, r+1, q)
                    q.pop()
                    cols.discard(c)
                    diag1.discard(r+c)
                    diag2.discard(r-c)
        recur(n, 0, [])
        res = []
        for sol in all_queen:
            board = []
            for i in range(n):
                rows = ["." for _ in range(n)]
                rows[sol[i]] = "Q"
                board.append("".join(rows[:]))
            res.append(board[:])

        return res