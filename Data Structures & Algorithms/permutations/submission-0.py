class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx, num):
            if idx >= len(num): 
                res.append(num[:])
                return
            for i in range(idx, len(num)):
                num[idx], num[i] = num[i], num[idx]
                dfs(idx+1, num)
                num[idx], num[i] = num[i], num[idx]
        dfs(0, nums)
        return res