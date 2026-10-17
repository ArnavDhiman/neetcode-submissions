class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def subset(i, s):
            if i >= len(nums):
                res.append(s[:])
                return
            s.append(nums[i])
            subset(i+1, s)
            s.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            subset(i+1, s)
        subset(0, [])
        return res