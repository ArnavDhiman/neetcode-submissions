class TimeMap:

    def __init__(self):
        self.mapper = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapper[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.mapper.get(key, [])

        start = 0
        end = len(val) - 1

        while start <= end:
            mid = start + (end-start)//2

            if val[mid][0] <=timestamp:
                res = val[mid][1]
                start = mid + 1

            else:
                end = mid-1
        return res