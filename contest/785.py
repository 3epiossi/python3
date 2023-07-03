class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) in {0,1}:
            return True
        A0 = set()
        B1 = set()
        def dfs(cur, where, stpas):
            if where == 0:
                A0.add(cur)
                if cur in A0 and cur in B1:
                    return False
            else:
                B1.add(cur)
                if cur in B1 and cur in A0:        
                    return False
            if cur in stpas:
                return True
            stpas.add(cur)
            for son in graph[cur]:
                    info = dfs(son, (where+1)%2, stpas)
                    if info == False:
                        return False
                    pass
            return True
        stpas = set()
        for cur in range(len(graph)):
            if cur not in A0 and cur not in B1:
                info = dfs(cur, 0, stpas)
                if info == False:
                    return False
                pass
            pass
        return True
        
        