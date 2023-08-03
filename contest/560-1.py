class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        cache = {}
        ret = 0
        for num in nums:
            upDate = {}
            for subSum in cache:
                upDate[num+subSum] = cache[subSum]
            upDate[num] = cache.get(0, 0)+1
            cache = upDate
            ret += cache.get(k, 0)
        return ret