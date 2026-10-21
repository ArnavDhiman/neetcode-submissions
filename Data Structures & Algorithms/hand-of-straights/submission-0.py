class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        if l%groupSize:
            return False

        count = Counter(hand)
        keys = sorted(list(count.keys()))
        k_idx = 0
        group = 0
        i =0
        loop = l//groupSize
        while k_idx < len(keys) and i < loop:
            key = keys[k_idx]
            group = groupSize
            i += 1
            while group:
                # print(count, key, i)
                group -= 1
                if key in count:
                    count[key] -= 1
                    if count[key] == 0:
                        del(count[key])
                        k_idx += 1
                    key += 1
                else:
                    return False

        return not count