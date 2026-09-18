class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        res = 1
        for n in nums:
            if n-1 not in s:
                c = 0
                while n+c in s:
                    c += 1
                res = max(c, res)
        return res