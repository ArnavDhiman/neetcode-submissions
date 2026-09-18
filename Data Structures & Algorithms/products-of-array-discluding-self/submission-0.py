class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1 for _ in nums]
        for i in range(1, len(nums)):
            l2r[i] = l2r[i-1]*nums[i-1]
        r = nums[-1]
        for j in range(len(nums)-2, -1, -1):
            l2r[j] *= r
            r *= nums[j]
        return l2r