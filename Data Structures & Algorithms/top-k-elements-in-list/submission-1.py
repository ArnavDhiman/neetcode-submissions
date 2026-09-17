from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for key,val in count.items():
            bucket[val].append(key)
        # print(bucket)

        res = []
        for i in range(len(nums), 0, -1):
            for v in bucket[i]:
                if len(res) == k:
                    return res
                res.append(v)
        return res