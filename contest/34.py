class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        m = 0
        while l < r and (nums[l] != target or nums[r] != target):
            m = (l+r)//2
            if nums[l] == target:
                r = m
                continue
            elif nums[r] == target:
                l = m+1
                continue
            if target <= nums[m]:
                r = m
            else:
                l = m+1
        if r == -1 or nums[r] != target : return [-1,-1]
        while l-1 >= 0 and nums[l-1] == target: l -= 1
        while r+1 < len(nums) and nums[r+1] == target: r += 1
        return [l,r]