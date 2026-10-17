class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        def recursion(l=0, r=0):
            if l > n or r > n:
                return
            if l == n and r == n:
                res.append("".join(s))
                return
            if l < n:
                s.append("(")
                recursion(l+1, r)
                s.pop()
            if r < l:
                s.append(")")
                recursion(l, r+1)
                s.pop()
        recursion()
        return res