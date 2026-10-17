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
        nums = []
        for d_idx in range(len(digits)):
            t = []
            if nums:
                for n in nums:
                    for i in num_map[digits[d_idx]]:
                        t.append(n+i)
            else:
                t = num_map[digits[d_idx]]
        # print(t)
            nums = t[:]
        
        return nums