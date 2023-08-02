class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length <= 10:
            return []
        cache = set()
        ret = set()
        for i in range(9,length):
            subS = s[i-9:i+1]
            if subS in cache:
                ret.add(subS)
            cache.add(subS)
        return ret