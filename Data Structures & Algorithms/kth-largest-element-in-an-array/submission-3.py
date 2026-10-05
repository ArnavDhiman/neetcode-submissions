import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k)
    def quick_select(self, nums, k):
        start = 0
        end = len(nums)-1
        kth = len(nums)-k
        # x = 0
        while start <= end: #and x < 7:
            small = start
            # x += 1
            pivot = random.randint(start, end)
            # swap
            print("Pivot -> ", pivot)
            nums[pivot], nums[end] = nums[end], nums[pivot]
            for i in range(start, end):
                if nums[i] <= nums[end]:
                    nums[i], nums[small] = nums[small], nums[i]
                    small += 1
            # print(nums, small, kth, start, end)
            # swap back again
            nums[small], nums[end] = nums[end], nums[small]
            if small == kth:
                return nums[small]
            if small < kth:
                start = small + 1
            else:
                end = small - 1
        return -1


    def using_heap(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]