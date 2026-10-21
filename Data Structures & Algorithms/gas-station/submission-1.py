class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        
        total_diff = 0
        res = 0
        curr_sum = 0
        for i in range(l):
            c =  gas[i]-cost[i]
            total_diff += c
            curr_sum += c

            if curr_sum < 0:
                curr_sum = 0
                res = i+1
            
        if total_diff < 0:
            return -1
        return res