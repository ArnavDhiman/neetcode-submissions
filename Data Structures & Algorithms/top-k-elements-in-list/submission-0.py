from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)

        for key, val in count.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)
            # print(heap)

        res = []
        while heap:
            val, key = heappop(heap)
            res.append(key)
        return res