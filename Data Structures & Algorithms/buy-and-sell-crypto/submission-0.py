class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for p in prices:
            res = max(res, p-buy)
            if p < buy:
                buy = p
        return res
