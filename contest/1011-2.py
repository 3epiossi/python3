class Solution:
def shipwithinDays(self, weights: List[int ], days: int) -> int:
    l, r =max(weights), sum(weights)
    res =r

    def canship(cap):
        ships, currcap = 1, cap
        for W in weights:
            if currcap - W < 0 :
                ships +=1
                currcap = cap
                currcap -= W
        return ships <= days

    while l <=r:
        cap = (1 +r) //2
        if canship(cap):
            res = min(res, cap)
            r= cap -1
        else:
            l=cap +1
        return res