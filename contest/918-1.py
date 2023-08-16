class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        length = len(nums)
        array = [set() for i in range(length)]
        tail = [nums[0]]
        array[0].add((nums[0], 0))
        maxRes = nums[0]
        for i in range(1,length):
            for prev, h in array[i-1]:
                new = prev+nums[i]
                array[i].add( (new, h) )
                maxRes = max(new, maxRes)
            tail.append(tail[-1]+nums[i])
            array[i].add( (nums[i], i) )
            maxRes = max(nums[i], maxRes)
        for t, latter in enumerate(tail):
            for front, h in array[-1]:
                if t < h: maxRes = max(maxRes, latter+front)
        return maxRes