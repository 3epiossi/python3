class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        lowerBound = ceil(sum(piles)/h)
        upperBound = max(piles)
        if length == h:
            return upperBound
        def canFinish(per):
            hourCost = 0
            i = 0
            while hourCost <= h:
                if i == length :
                    if hourCost > h:
                        return False
                    return True
                hourCost += ceil(piles[i]/per)
                i += 1
            return False
        while upperBound > lowerBound:
            k = (lowerBound+upperBound)//2
            if canFinish(k):
                upperBound = k
            else:
                lowerBound = k+1
        return upperBound