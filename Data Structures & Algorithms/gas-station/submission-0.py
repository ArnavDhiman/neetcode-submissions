class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        diff_arr = [0 for _ in range(l)]
        total_diff = 0
        for i in range(l):
            diff_arr[i] = gas[i]-cost[i]
            total_diff += diff_arr[i]
        
        if total_diff < 0:
            return -1

        res = 0
        curr_sum = 0
        for i in range(l):
            if curr_sum < 0:
                curr_sum = diff_arr[i]
                res = i
            else:
                curr_sum += diff_arr[i]
            # print(curr_sum, i, res)
        return res