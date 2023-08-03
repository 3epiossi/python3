class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0:1}
        sumOfCur = 0
        ret = 0
        for num in nums:
            sumOfCur += num
            ret += cache.get(sumOfCur-k, 0)
            cache[sumOfCur] = cache.get(sumOfCur, 0)+1
        return ret