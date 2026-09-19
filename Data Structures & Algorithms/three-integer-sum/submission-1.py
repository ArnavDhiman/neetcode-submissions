class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            if nums[i] > 0:
                break
            target = -nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    k_num = nums[k]
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while k > j and nums[k] == k_num:
                        k -= 1
            while i < len(nums) and nums[i] == -target:
                i += 1
        return res
                