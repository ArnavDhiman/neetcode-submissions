class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        l2r = [0 for _ in range(l)]
        r2l = [0 for _ in range(l)]

        for i in range(l):
            l2r[i] = max(height[i], l2r[i-1])
            r2l[l-1-i] = max(height[l-1-i], r2l[min(l-1, l-i)])
        res = 0
        for i in range(l):
            res += max(0, min(l2r[i], r2l[i]) - height[i])
        # print(l2r, r2l)
        return res