class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        diff = [(costs[i][1]-costs[i][0], i) for i in range(length)]
        diff.sort()
        res = 0
        for j,(d,i) in enumerate(diff):
            if j < length//2: res += costs[i][1]
            else: res += costs[i][0]
        return res