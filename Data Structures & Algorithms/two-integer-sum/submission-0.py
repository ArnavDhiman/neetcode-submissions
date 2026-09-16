class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.optimal(nums, target)

    def bruteForce(self, nums, target):
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[i+1:]):
                if n1+n2 == target:
                    return [i,i+j+1]
        return [-1, -1]

    def optimal(self, nums, target):
        lookup = {}
        for i, n in enumerate(nums):
            if target-n in lookup:
                return [lookup[target-n], i]
            lookup[n] = i
        return [-1, -1]