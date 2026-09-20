class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        res = 0
        seen = collections.defaultdict(int)
        while i < len(s):
            if s[i] in seen:
                j = max(j, seen[s[i]]+1)
            res = max(res, i-j+1)
            seen[s[i]] = i
            i += 1
        return res