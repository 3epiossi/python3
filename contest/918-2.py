class Solution: #kadane's algo
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxRes = -math.inf
        minSubt = 0
        prefix = 0
        nPrefix = 0
        total = 0
        for num in nums:
            minSubt = min(nPrefix+num, minSubt)
            nPrefix = min(nPrefix+num, 0)
            maxRes = max(prefix+num, maxRes)
            prefix = max(0, prefix+num)
            total += num
        
        if minSubt < 0 and total-minSubt > maxRes and total != minSubt:
            return total-minSubt
        else:
            return maxRes