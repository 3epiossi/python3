class solution:
    def mincostconnectpoints(self, points: list[list[int]]) -> int:
        from collections import defaultdict
        from heapq import heappush
        cache = defaultdict(list)
        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                cache[i].append((dist, j))
                cache[j].append((dist, i))
        ret = 0
        minheap = [[0,0]]
        stpass = set([0])
        while len(stpass) < n:
            curcost, cur = minheap.pop()
            stpass.add(cur)
            ret += curcost
            for frontcost, front in cache[cur]:
                if front not in stpass:
                    heappush(minheap, [frontcost, front])
        return ret