class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for fm, to, pr in flights:
            adj[fm].append( (pr, to) )
        
        record = {(src,0):0}
        curReach = set([src])
        pas = set([src])
        for i in range(1, k+2):
            nextReach = set()
            for cur in curReach:
                for pr, son in adj[cur]:
                    record[(son,i)] = min(record.get((son,i), math.inf), record[(cur,i-1)]+pr)
                    nextReach.add(son)
            curReach = nextReach
        res = min([record.get( (dst, i), math.inf ) for i in range(k+2)])
        return res if res != math.inf else -1 
