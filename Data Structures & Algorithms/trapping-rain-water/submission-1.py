class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        i, j = 0, l-1
        res = 0
        r_max = height[0]
        l_max = height[-1]
        while i < j:
            if r_max <= l_max:
                i += 1
                res += max(0, min(r_max, l_max)-height[i])
                r_max = max(r_max, height[i])
            else:
                j -= 1
                res += max(0, min(r_max, l_max)-height[j])
                l_max = max(l_max, height[j])
        return res