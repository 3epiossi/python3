class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dtG = {i:[] for i in range(numCourses)}
        for edge in prerequisites:
            dtG[edge[1]].append(edge[0])
        dtpc = {}
        def dfs(cur):
            if dtG[cur] == []:
                return {cur}
            stret = set()
            stret.add(cur)
            for son in dtG[cur]:
                if son not in dtpc:
                    dtpc[son] = dfs(son)
                    stret.update(dtpc[son])
                else:
                    stret.update(dtpc[son])
            dtpc[cur] = stret
            return stret
        
        for node in range(numCourses):
            if node not in dtpc:
                dtpc[node] = dfs(node)
            pass
        ltbool = [True for i in range(len(queries))]
        ct = 0
        for q in queries:
            if  q[0] not in dtpc[q[1]]:
                ltbool[ct] = False
            ct += 1
        return ltbool

        