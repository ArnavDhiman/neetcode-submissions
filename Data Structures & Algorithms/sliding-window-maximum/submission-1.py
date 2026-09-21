class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[0], 0)]
        for i in range(1, k):
            heapq.heappush(heap, (-nums[i], i))
        # print(heap)
        res = []
        res.append(-heap[0][0])
        
        for i in range(k, len(nums)):
            # print(i)

            heapq.heappush(heap, (-nums[i], i))
            while heap and heap[0][1] <= i-k:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
        return res