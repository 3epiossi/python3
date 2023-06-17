class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        idl, idr = 0, 0
        ltret = []
        while True:
            if idl == len(nums):
                break
            idr = idl
            while idr+1 != len(nums) and nums[idr+1] == nums[idr]+1:
                idr += 1
            ltret.append("{}->{}".format(nums[idl], nums[idr]) if idl != idr else "{}".format(nums[idl]))
            idl = idr+1
        return ltret