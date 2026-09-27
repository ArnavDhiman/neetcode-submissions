class Solution:
    def findMin(self, nums: List[int]) -> int:
        # possibilities
        
        # start > end -> rotated
        # else -> not rotated


        start = 0
        end = len(nums)-1
        # i = 0
        while start < end:
            # i += 1
            mid = start + (end-start)//2
            # print(nums[start], nums[mid], nums[end], mid)
            if nums[start] > nums[end]:
                if nums[mid] < nums[end]:
                    end = mid
                else:
                    start = mid + 1
            else:
                end = mid
        return nums[end]
                  