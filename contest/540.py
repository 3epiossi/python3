class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        r = len(nums)-1
        l = 0
        while l != r:
            m = (l+r)//2
            if nums[m-1] != nums[m]:
                m -= 1
            if (m+1)%2 == 1:
                r = m
            else:
                l = m+1
        return nums[l]