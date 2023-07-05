class Solution:
    def rob(self, nums: List[int]) -> int:
        pas = [0, 0]
        nopas = [0, 0]
        for val in nums:
            cur2pas = nopas[-1]+val
            curnopas = max(pas[-1], pas[-2])
            pas.append(cur2pas)
            nopas.append(curnopas)
        return max(pas[-1], nopas[-1])