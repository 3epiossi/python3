class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        strsMN = []
        for s in strs:
            strsMN.append( (s.count('0'),s.count('1')) )    
        cache = {(0,0,0)}
        res = 0
        for curM, curN in strsMN:
            curSet = set()
            for step, countM, countN in cache:
                if countM+curM <= m and countN+curN <= n:
                    curSet.add( (step+1, countM+curM, countN+curN) )
            cache |= curSet
        return max(cache)[0]