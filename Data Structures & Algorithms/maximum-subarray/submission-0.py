class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [-float("inf") for _ in range(len(nums))]
        res[0] = nums[0]
        ans = res[0]
        for i in range(1, len(nums)):
            if res[i-1] + nums[i] >= nums[i]:
                res[i] = res[i-1]+nums[i]
            else:
                res[i] = nums[i]
            ans = max(ans, res[i])
        # print(res)
        return ans