class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] < newInterval[0]:
                res.append(intervals[i])
            else:
                break
            i+=1
        # print(res)
        if res and res[-1][1] >= newInterval[0]:
            res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval)
        # print(res)
        while i < len(intervals):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i += 1
            # print(res)
        return res