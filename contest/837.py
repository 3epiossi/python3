class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n > k+maxPts:
            return 1
        dtdp = {}
        ct = 0
        for i in range(k, k+maxPts):
            if i <= n:
                dtdp[i] = 1
                ct += 1
            else:
                dtdp[i] = 0
        for step in range(k-1, 0-1, -1):
            dtdp[step] = ct/maxPts
            ct = ct - dtdp[step+maxPts] + dtdp[step] 
        return dtdp[0]