class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqs = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    sq = self.getsq(i,j)
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sqs[sq]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sqs[sq].add(board[i][j])
        return True

    def getsq(self, i, j):
        if i < 3:
            if j < 3: return 1
            if j < 6: return 2
            return 3
        if i < 6:
            if j < 3: return 4
            if j < 6: return 5
            return 6
        if j < 3: return 7
        if j < 6: return 8
        return 9