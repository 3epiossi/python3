class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cache = {(0,0):0}
        length = len(costs)
        for costA, costB in costs:
            new = {}
            for countA, countB in cache:
                if countA < length/2:
                    new[(countA+1, countB)] = min(cache[(countA, countB)]+costA,new.get((countA+1, countB), 10**9))
                if countB < length/2:
                    new[(countA, countB+1)] = min(cache[(countA, countB)]+costB,new.get((countA, countB+1), 10**9))
            cache = new
        return min(cache.values())