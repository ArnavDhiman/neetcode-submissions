class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            i1 = i
            while stack and stack[-1][0] > h:
                h1, i1 = stack.pop(-1)
                res = max(res, h1*(i-i1))
            stack.append((h, i1))
            # print(stack, res)
        l = len(heights)
        while stack:
            h1, i1 = stack.pop(-1)
            res = max(res, h1*(l-i1))
            # print("FINAL -> ",stack, res)
        return res