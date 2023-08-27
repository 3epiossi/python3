class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key= lambda x: x[1])
        upper = -1001
        count = 0
        for l, r in pairs:
            if l > upper:
                upper = r
                count += 1
        return count