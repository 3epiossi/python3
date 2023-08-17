class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append( (w, v) )
        que = [(0, k)]
        accu = {}
        pas = set()
        count = 0
        while que:
            wei, cur = heapq.heappop(que)
            accu[cur] = wei
            if cur not in pas: 
                pas.add(cur)
                count += 1
            if count == n: return max(accu.values())
            for w, son in adj[cur]:
                if son not in accu:
                    heapq.heappush(que, (wei+w, son) )
        return -1