class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_c = Counter(s1)
        i = 0
        l1 = len(s1)
        while i < len(s2)-l1+1:
            tmp = s2[i:i+l1]
            # print(tmp)
            tmp_c = Counter(tmp)
            if s1_c == tmp_c:
                return True
            i+=1
        return False