class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        if length == 1: return nums
        nums[0], nums[1] = (nums[1], nums[0]) if nums[0] > nums[1]\
                      else (nums[0], nums[1])
        for i in range(2,length):
            l, r = 0, i-1
            temp = nums.pop(i)
            while l < r:
                m = (l+r)//2
                if temp <= nums[m]:
                    r = m
                else:
                    l = m+1
            if temp <= nums[l]:
                nums.insert(l, temp)
            else:
                nums.insert(l+1, temp)
        return nums