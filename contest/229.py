class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cache = collections.defaultdict(int)
        wantDel = []
        for i in nums:
            while len(cache) > 2:
                wantDel.clear()
                for ele in cache:
                    cache[ele] -= 1
                    if cache[ele] <= 0:
                        wantDel.append(ele)
                for d in wantDel:
                    del cache[d]
            cache[i] += 1
        res = []
        for possible in cache:
            if nums.count(possible) > len(nums)//3:
                res.append(possible)
        return res