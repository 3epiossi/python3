class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dtdp = {}
        def dfs(vec):
            if vec > high:
                return 0
            if vec in dtdp:
                return dtdp[vec]
            if low <= vec <= high:
                dtdp[vec] = dtdp.get(vec, 0) + 1
            
            dtdp[vec] = (dtdp.get(vec, 0)+dfs(vec+zero)+dfs(vec+one))%(10**9+7)
            return dtdp[vec]
        return dfs(0) % (10**9 + 7)