class Solution:
    def jump(self, nums: List[int]) -> int:
        heap = [(0,0)]
        seen = set()
        steps = 0
        while heap:
            # print(heap)
            steps, idx = heapq.heappop(heap)
            if idx >= len(nums)-1:
                return steps
            for i in range(nums[idx]):
                if idx+i+1 not in seen:
                    heapq.heappush(heap, (steps+1, idx+i+1))
                    seen.add(idx+i+1)
                    if idx+i+1 >= len(nums)-1:
                        return steps+1
        return steps