class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        step1 = 2
        step2 = 1
        n-=2
        while n > 0:
            step1, step2 = step1+step2, step1
            n -= 1
            # print(step1, step2, step1+step2)
        return step1