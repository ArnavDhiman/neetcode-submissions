class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start < end:
            mid = start + (end-start)//2
            hours = self.get_hours(piles, mid)
            # print(mid, hours)
            if hours > h:
                start = mid+1
            else:
                end = mid
        return start

    def get_hours(self, piles, rate):
        s = 0
        for pile in piles:
            s += math.ceil(pile/rate)
        return s