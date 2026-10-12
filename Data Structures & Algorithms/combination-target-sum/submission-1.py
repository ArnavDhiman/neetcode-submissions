class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(arr, rem, idx):
            if rem < 0:
                return
            if rem == 0:
                res.append(arr[:])
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                dfs(arr, rem-nums[i], i)
                arr.pop()
            
        dfs([], target, 0)
        return res