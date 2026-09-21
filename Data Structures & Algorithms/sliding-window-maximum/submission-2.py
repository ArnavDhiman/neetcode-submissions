class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.mono_queue(nums, k)
    def mono_queue(self, nums, k):
        res = []
        q = deque()

        for i, n in enumerate(nums):
            while q and q[0][1] <= i-k:
                q.popleft()
            while q and q[-1][0] < n:
                q.pop()
            q.append((n,i))
            # print(q, i)
            if i >= k-1:
                res.append(q[0][0])
        return res
        # pass
    def heap_sol(self, nums, k):
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