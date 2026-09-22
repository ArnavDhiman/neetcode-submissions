class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.moving(s, t)
    def moving(self, s, t):
        want = 0
        need = 0

        want_map = collections.defaultdict(int)
        need_map = {}

        for c in t:
            need_map[c] = 0
            want_map[c] += 1
        want = len(need_map)
        i = 0
        j = 0
        res = [-1, -1]
        while i < len(s):
            if s[i] in need_map:
                need_map[s[i]] += 1
                if need_map[s[i]] == want_map[s[i]]:
                    need += 1
            while want == need:
                # print("YESS")
                if res[0] == -1:
                    res[0] = j
                    res[1] = i
                else:
                    if res[1] - res[0] + 1 > i - j + 1:
                        res[0] = j
                        res[1] = i
                
                if s[j] in need_map:
                    need_map[s[j]] -= 1
                    # print(i, j)
                    if need_map[s[j]] < want_map[s[j]]:
                        need -= 1
                j += 1
            i+=1
        return s[res[0]: res[1]+1]



    def sub_optimal(self, s, t):
        res = ""
        if len(s) < len(t):
            return res
        i = 0
        j = 0
        min_val = len(s)
        t_c = Counter(t)
        s_ind = collections.defaultdict(list)
        while i < len(s) and s[i] not in t_c:
            i += 1
            j += 1
        # print(i)
        # i -= 1
        while i < len(s):
            if s[i] in t_c:
                t_c[s[i]] -= 1
                s_ind[s[i]].append(i)
            while all(val <= 0 for val in t_c.values()):
                if i-j+1 <= min_val:
                    min_val = i-j+1
                    res = s[j:i+1]
                if len(res) == len(t):
                    return res
                min_ind = i
                min_chr = ""
                for k, v in s_ind.items():
                    if v and v[0] < min_ind:
                        min_ind = v[0]
                        min_chr = k
                s_ind[min_chr].pop(0)
                t_c[min_chr] += 1
                
                min_ind = i
                for k, v in s_ind.items():
                    if v and v[0] < min_ind:
                        min_ind = v[0]
                j = min_ind
            i += 1
        return res