class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dtadj = {}
        lttmp = list(zip(*equations))
        for i in lttmp[0]:
            dtadj[i] = []
        for i in lttmp[1]:
            dtadj[i] = []
        ltans = []
        ct = 0
        for equa in equations:
            dtadj[equa[0]].append((equa[1], values[ct]))
            dtadj[equa[1]].append((equa[0], 1/values[ct]))
            ct += 1
        dtdp = {}
        def dfs(cur, dep, tar, val, ltpas):
            dtdp[(dep, cur)] = val
            if cur in ltpas:
                return -1
            if (cur, tar) in dtdp:
                ltans.append(dtdp[(cur, tar)]*val)
                return 1
            if cur == tar:
                ltans.append(val)
                return 1
            ltpas.append(cur)
            for son, val2 in dtadj[cur]:
                info = dfs(son, dep, tar, val*val2, ltpas)
                if info != -1:
                    return 1
            return -1
        
        for dep, tar in queries:
            if dep not in dtadj or tar not in dtadj:
                ltans.append(-1)
                continue
            if dep == tar:
                ltans.append(1)
                continue
            ltpas = []
            val = 1
            info = dfs(dep, dep, tar, val, ltpas)
            if info == -1:
                ltans.append(-1)
        return ltans