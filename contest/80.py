class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head, tail = 0, 0
        length = len(nums)
        while tail < length:
            count = 1
            while tail+1 < length and nums[tail+1] == nums[tail]:
                tail += 1
                count += 1
            for _ in range(min(2, count)):
                nums[head] = nums[tail]
                head += 1
            tail += 1
        return head