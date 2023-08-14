class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        rightEnd = set()
        for i in range(len(nums)):
            res = []
            if i-1 >= 0 and nums[i-1] == nums[i]:
                res.append( (i-1,i+1) )
            if i-2 >= 0 and nums[i-2] == nums[i-1] and nums[i-1] == nums[i]:
                res.append( (i-2,i+1) )
            if i-2 >= 0 and nums[i-2]+1 == nums[i-1] and nums[i-1]+1 == nums[i]:
                res.append( (i-2,i+1) )
            for a, b in res:
                if a == 0 or a in rightEnd:
                    rightEnd.add(b)
        return True if len(nums) in rightEnd else False