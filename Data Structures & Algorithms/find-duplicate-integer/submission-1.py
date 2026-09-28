class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        # print(n)
        for i in range(n):
            idx = nums[i]*-1 if nums[i] < 0 else nums[i]
            # print(nums, idx, i, nums[i])
            if nums[idx] < 0:
                return idx
            nums[idx] *= -1
        return -1