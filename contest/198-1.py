class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(cur, parinfo):
            if cur >= len(nums):
                return 0
            if parinfo:
                cache[(cur, parinfo)] = dfs(cur+1, False)
                return cache[(cur, parinfo)]
            cache[(cur, parinfo)] = max(dfs(cur+1, False), nums[cur]+dfs(cur+1, True))
            return cache[(cur, parinfo)]
        return max(dfs(0, True), dfs(0, False))