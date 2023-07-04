class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        total = sum(stones)
        half = ceil(total/2)
        dtcache = {}
        def dfs(cur, cursum):
            if cur >= len(stones) or cursum >= half:
                return abs(cursum-(total-cursum))
            if (cur, cursum) in dtcache:
                return dtcache[(cur, cursum)]
            dtcache[(cur,cursum)]=min(dfs(cur+1, cursum), dfs(cur+1, cursum+stones[cur]))
            return dtcache[(cur, cursum)]
        return dfs(0,0)

        