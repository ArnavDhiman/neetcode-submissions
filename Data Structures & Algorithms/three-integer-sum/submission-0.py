class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        i = 0
        while i < len(nums):
            num = nums[i]
            target = -num
            tmp = self.two_sum(nums, i, target)
            for t in tmp:
                res.add(tuple(sorted([num, t[0], t[1]])))
            while i < len(nums) and nums[i] == num:
                i += 1

        # res = []
        # for k, v in mapper:
        #     res.append((k, v[0], v[1]))
        return list(res)

    def two_sum(self, nums, i, target):
        res = set()
        hmap = {}
        for j, n in enumerate(nums):
            if i != j:
                if target-n in hmap:
                    res.add(tuple(sorted([n, target-n])))
                hmap[n] = j
        return res