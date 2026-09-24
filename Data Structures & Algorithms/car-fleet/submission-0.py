class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x: (x[0], x[1]))
        stack = []
        for i in range(len(cars)):
            t1 = (target-cars[i][0])/cars[i][1]
            while stack and (target-stack[-1][0])/stack[-1][1] <= t1:
                stack.pop()
            stack.append(cars[i])
        return len(stack)