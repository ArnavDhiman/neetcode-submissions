class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = [0 for _ in range(26)]
        for c in s:
            hmap[ord(c)-ord('a')] += 1
        for c in t:
            hmap[ord(c)-ord('a')] -= 1
            if hmap[ord(c)-ord('a')] < 0:
                return False
        return sum(hmap) == 0
        