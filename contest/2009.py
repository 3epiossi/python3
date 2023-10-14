class Solution:
    def minOperations(self, nums: list[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums)) #若nums[l] == nums[l+1] == nums[l+2],只有一個不會動，其他都會動
        r = 0
        res = length
        for l in range(len(nums)):
            while r < len(nums) and nums[r] < nums[l]+length:
                r += 1
            window = r-l
            res = min(res, length-window) #window內的不會動，其他的都會動
        return res
