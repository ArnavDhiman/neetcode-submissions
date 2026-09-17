class Solution:
    def __init__(self):
        self.__SPCHAR = "%1%"

    def encode(self, strs: List[str]) -> str:
        tmp = ""
        if strs:
            strs = [" "] + strs
            tmp = self.__SPCHAR.join(strs)
        return tmp

    def decode(self, s: str) -> List[str]:
        if s:
            return s.split(self.__SPCHAR)[1:]
        return []