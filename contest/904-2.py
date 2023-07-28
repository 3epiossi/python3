class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cata = collections.defaultdict(int)
        subLen = 0
        ret = 0
        l, r = 0, 0
        for r in range(len(fruits)):
            cata[fruits[r]] += 1
            subLen += 1
            while len(cata) > 2:
                cata[fruits[l]] -= 1
                subLen -= 1
                if cata[fruits[l]] == 0:
                    del cata[fruits[l]]
                l += 1
            ret = max(ret, subLen)
        return ret