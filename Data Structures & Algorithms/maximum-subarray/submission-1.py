class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        ans = res
        for i in range(1, len(nums)):
            if res + nums[i] >= nums[i]:
                res = res+nums[i]
            else:
                res = nums[i]
            ans = max(ans, res)
        return ans