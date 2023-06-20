class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = []
        lest, rest = k, len(nums) -1-k
        l, r = 0, 2*k
        length = len(nums)
        if 2*k > length-1:
            avgs.extend([-1]*(length))
            return avgs
        avgs.extend([-1]*k)
        for i in range(lest, rest+1):
            avg = sum(nums[i-k:i+k+1])//(2*k+1)
            avgs.append(avg)
        avgs.extend([-1]*k)
        return avgs