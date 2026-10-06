class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.head = TreeNode()        
        self.create_trie(words)
        self.res = []
        self.neig = [[0,1],[1,0],[0,-1],[-1,0]]
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        # print(self.head.hmap)
        for i in range(self.rows):
            for j in range(self.cols):
                # print(i,j, board[i][j])
                if board[i][j] in self.head.hmap:
                    self.dfs(i, j,self.head.hmap[board[i][j]])
                    # print(self.board)
        return self.res


    def dfs(self, i, j, node):
        tmp = self.board[i][j]
        self.board[i][j] = "#"
        if node.is_end:
            self.res.append(node.word)
            node.is_end = False
        
        for ni, nj in self.neig:
            di,dj = i+ni, j+nj
            if 0 <= di < self.rows and 0 <= dj < self.cols and self.board[di][dj] in node.hmap:
                # print(tmp, self.board[di][dj])
                self.dfs(di,dj,node.hmap[self.board[di][dj]])
        self.board[i][j] = tmp

    def create_trie(self, words):
        for word in words:
            node = self.head
            for c in word:
                if c not in node.hmap:
                    node.hmap[c] = TreeNode()
                node = node.hmap[c]
            node.is_end = True
            node.word = word

class TreeNode:
    def __init__(self):
        self.hmap = {}
        self.word = ""
        self.is_end = False