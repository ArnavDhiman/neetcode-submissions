class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if not nums:
            return 0
        res = 1
        for n in nums:
            if n-1 in s and n+1 not in s:
                c = 0
                while n in s:
                    c += 1
                    n -= 1
                res = max(c, res)
        return res