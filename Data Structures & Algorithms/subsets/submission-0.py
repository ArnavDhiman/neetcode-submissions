class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        def recur(idx):
            if idx >= len(nums):
                res.append(tmp.copy())
                return
            tmp.append(nums[idx])
            recur(idx+1)
            tmp.pop()
            recur(idx+1)
        
        recur(0)
        return res