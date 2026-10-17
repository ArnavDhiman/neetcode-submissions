class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        nei = [[0,1],[1,0],[0,-1],[-1,0]]
        def recursion(i,j,word_idx):
            if word_idx == len(word):
                return True
            # print(word_idx)
            for ni, nj in nei:
                di, dj = i+ni, j+nj
                # print(di, dj, word[word_idx])
                if 0 <= di < rows and 0 <= dj < cols and board[di][dj] == word[word_idx]:
                    tmp = board[di][dj]
                    board[di][dj] = "-"
                    # print(word_idx, di, dj, board)
                    if word_idx == len(word)-1:
                        return True
                    if recursion(di, dj, word_idx+1):
                        return True
                    board[di][dj] = tmp
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    tmp = board[r][r]
                    board[r][c] = "-"

                    if recursion(r, c, 1):
                        return True
                    board[r][c] = tmp
        return False