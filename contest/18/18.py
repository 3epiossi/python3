class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        test3 = sum(nums[:3])
        cache = set()
        ret = set()
        for num in nums:
            if num+test3 > target:
                return ret
            temp = set()
            gonnaPop = set()
            for sub in cache:
                if len(sub) == 3:
                    subSum = sum(sub)+num
                    new = [*sub, num]
                    if subSum > target:
                        gonnaPop.add(sub)
                    elif subSum == target:
                        ret.add(tuple(new))
                    continue
                elif len(sub) < 3:
                    new = [*sub, num]
                    temp.add(tuple(new))
            cache.update(temp)
            cache -= gonnaPop 
            cache.add((num, ))
        return ret