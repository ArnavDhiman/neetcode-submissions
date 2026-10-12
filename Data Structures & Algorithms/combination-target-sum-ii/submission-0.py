class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(arr, rem, idx):
            if rem == 0:
                res.append(arr[:])
                return 

            for i in range(idx, len(candidates)):
                if rem - candidates[i] < 0:
                    continue
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                dfs(arr, rem-candidates[i], i+1)
                arr.pop()

        dfs([], target, 0)
        return res