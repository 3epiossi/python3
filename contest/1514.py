class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))
        dijk = [(-1, start_node)]
        pas = set()
        while dijk:
            start2cur, cur = heapq.heappop(dijk)
            if cur == end_node:
                return -start2cur
            pas.add(cur)
            for son, cur2son in adj[cur]:
                if son not in pas:
                    heapq.heappush(dijk, (start2cur*cur2son, son))
        return 0