class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        i = 0
        while i < len(pairs):
            if i+1 < len(pairs) and pairs[i+1][0] == pairs[i][0]:
                pairs.pop(i+1)
            else:
                i += 1
        pairs.reverse()
        i = 0
        while i < len(pairs):
            j = i+1
            while j < len(pairs):
                if pairs[j][1] >= pairs[i][1]:
                    pairs.pop(j)
                else:
                    j += 1
            i += 1
        lower = 1001
        count = 0
        for l, r in pairs:
            if r < lower:
                lower = l
                count += 1
        return count