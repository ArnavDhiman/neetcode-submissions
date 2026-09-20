class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_c = Counter(s1)
        l1 = len(s1)
        for i in range(l1):
            if s2[i] in s1_c:
                s1_c[s2[i]] -= 1
        if all(value == 0 for value in s1_c.values()):
            return True
        for i in range(l1, len(s2)):
            remove = s2[i-l1]
            add = s2[i]
            if remove in s1_c:
                s1_c[remove] += 1
            if add in s1_c:
                s1_c[add] -= 1
            if all(value == 0 for value in s1_c.values()):
                return True
        return False
