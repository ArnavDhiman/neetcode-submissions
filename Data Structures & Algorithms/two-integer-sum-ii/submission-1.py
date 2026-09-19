class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            tmp = - 1
            if target - numbers[i] <= numbers[i]:
                tmp = self.binary_search(numbers, target - numbers[i], 0, i)
                if tmp >= 0:
                    return[tmp+1, i+1]
            else:
                tmp = self.binary_search(numbers, target - numbers[i], i, len(numbers)-1)
                if tmp >= 0:
                    return[i+1, tmp+1]
        return [-1, -1]
    def binary_search(self, nums, target, start, end):
        while start < end:
            # print(start, end, target)
            mid = start + (end-start)//2

            if nums[mid] == target: return mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return -1