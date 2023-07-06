class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        if half-int(half) != 0:
            return False
        if half in nums:
            return True
        nums.sort(reverse=True)
        cache = {-1:{0}}
        for i, cur in enumerate(nums):
                cache[i] = set()
                st = set(map(lambda x:x+cur, cache[i-1]))
                cache[i].update(st)
                if half in cache[i]:
                    return True
                cache[i].update(cache[i-1])
        return False
            

            