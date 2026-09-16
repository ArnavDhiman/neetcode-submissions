from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            key = [0 for _ in range(26)]
            for c in word:
                key[ord(c)-ord('a')] += 1
            hmap[tuple(key)].append(word)
            # print(key, hmap)
        return list(hmap.values())