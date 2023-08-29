class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums.insert(0, 10**-5)
        nums.append(10**5)
        length = len(nums)
        i = 1
        while i < length-1 and nums[i] <= nums[i+1]: 
            i += 1
        if i >= length-1:
            return True
        elif nums[i-1] > nums[i+1]:
            if i+2 < length and nums[i+2] >= nums[i]:
                i += 2
                while i < length-1 and nums[i] <= nums[i+1]:
                    i += 1
                if i >= length-1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            i += 1
            while i < length-1 and nums[i] <= nums[i+1]:
                i += 1
            if i >= length-1:
                return True
            else:
                return False