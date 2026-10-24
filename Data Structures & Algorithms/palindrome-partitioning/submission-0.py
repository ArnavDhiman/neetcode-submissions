class Solution:
    def partition(self, s: str) -> List[List[str]]:
        tmp = []
        res = []
        self.palin = {}
        def recursion(start, end):
            # print(start, end, tmp)
            if end >= len(s):
                if end == start:
                    res.append(tmp[:])
                return
            if self.is_palindrome(s[start:end+1]):
                tmp.append(s[start:end+1])
                recursion(end+1, end+1)
                tmp.pop()
            recursion(start, end+1)
        recursion(0,0)
        return res
        
        
    def is_palindrome(self, s):
        res = True
        if s not in self.palin:
            i, j = 0, len(s)-1
            while i<j:
                if s[i] != s[j]:
                    res = False
                    break
                i += 1
                j -= 1
            self.palin[s] = res
        return self.palin[s]