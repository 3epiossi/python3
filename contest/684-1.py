class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cache = list()
        for a, b in edges:
            ixa, ixb = -1, -2
            for ixSubset in range(len(cache)):
                if a in cache[ixSubset]:
                    ixa = ixSubset
                if b in cache[ixSubset]:
                    ixb = ixSubset
                if ixa == ixb:
                    return [a, b]
            if ixa == -1 and ixb == -2:
                cache.append({a, b})
            elif ixa == -1 and ixb != -2:
                cache[ixb].add(a)
            elif ixa != -1 and ixb == -2:
                cache[ixa].add(b)
            else:
                cache[ixa].update(cache[ixb])
                del cache[ixb]