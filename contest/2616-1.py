class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        length = len(nums)
        if p == 0 or length < 2:
            return 0
        nums.sort()
        diff = []
        for i in range(length-1):
            d = abs(nums[i+1] - nums[i])
            diff.append(d)
        length = len(diff)
        prev2 = {(0,0)}
        prev1 = {(0,0)}
        maxMin = 10**9+1
        for i in range(length):
            cur = set()
            for ct, mx in prev2:
                if ct+1 >= p:
                    maxMin = min(maxMin, max(mx,diff[i]))
                    continue
                cur.add((ct+1,max(diff[i], mx)))
            cur.update(prev1)
            prev2 = prev1
            prev1 = cur
        return maxMin