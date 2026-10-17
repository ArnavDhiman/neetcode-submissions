class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursion(l=0, r=0, s=""):
            if l > n or r > n:
                return
            if l == n and r == n:
                res.append(s[:])
                return
            if l < n:
                recursion(l+1, r, s+"(")
            if r < l:
                recursion(l, r+1, s+")")
        recursion()
        return res