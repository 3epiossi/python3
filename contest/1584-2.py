class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        from collections import defaultdict
        from heapq import heappush, heappop
        cache = defaultdict(list)
        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                cache[i].append((dist, j))
                cache[j].append((dist, i))
        ret = 0
        minHeap = [[0,0]]
        stPass = set()
        while len(stPass) < n:
            curCost, cur = heappop(minHeap)
            if cur in stPass:
                continue # 原先在heap中就有了, 後面的front並沒有阻止
            stPass.add(cur)
            ret += curCost
            for frontCost, front in cache[cur]:
                if front not in stPass:
                    heappush(minHeap, [frontCost, front])
        return ret