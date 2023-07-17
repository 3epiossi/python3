class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        from collections import defaultdict, deque
        cache = defaultdict(list)
        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                cache[i].append((j , dist))
                cache[j].append((i , dist))
        pas = set([0])
        ret = 0
        while len(pas) < n:
            minIx, minVal = 2**31-1, 2**31 - 1
            for front in pas:
                for son , val in cache[front]:
                    if son not in pas:
                        if val < minVal :
                            minIx = son
                            minVal = val
            ret += minVal
            pas.add(minIx)
        return ret