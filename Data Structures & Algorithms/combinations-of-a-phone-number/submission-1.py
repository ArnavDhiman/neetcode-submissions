class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z'],
        }
        res = []
        def recur(nums, d_idx):
            if d_idx == len(digits):
                res.append(nums)
                return
            for c in num_map[digits[d_idx]]:
                recur(nums+c, d_idx+1)            
        if digits:
            recur("", 0)
        return res 
        