class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t1, i1 = stack.pop()
                res[i1] = i-i1
            stack.append((temp, i))
        return res