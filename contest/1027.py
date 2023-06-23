class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        maxret = 2
        cache = dict()
        for idf in range(n):
            if idf not in cache:
                cache[idf] = []
            for ids in range((idf+1), n):
                if idf in cache:
                    if ids in cache[idf]:
                        continue
                    else:
                        cache[idf].append(ids)
                d = nums[ids] - nums[idf]
                idfol = ids
                t = 2
                
                while True:
                    try:
                        idfol = nums.index( nums[idfol]+d , idfol+1, n)
                        t += 1
                    except:
                        break
                if maxret < t:
                    maxret = t
                pass
            pass
        return maxret