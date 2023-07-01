class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        length = len(bombs)
        dtadj = {i:[] for i in range(length)}
        for i in range(length):
            for j in range(i,length):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                if d <= r1:
                    dtadj[i].append(j)
                if d <= r2:
                    dtadj[j].append(i)
                pass
            pass

        def dfs(cur, stpas):
            if cur in stpas:
                return 0
            stpas.add(cur)
            sub = 0
            for son in dtadj[cur]:
                sub += dfs(son, stpas)
            return sub + 1
        ret = 0
        for cur in range(length):
            stpas = set()
            detonate = dfs(cur, stpas)
            if ret < detonate:
                ret = detonate
                pass
            pass    
        return ret