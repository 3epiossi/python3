class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        tot = sum(weights)
        if days == 1:
            return tot
        length = len(weights)
        goal = ceil(tot/days)
        cache = {}
        
        while True:
            remainDay = days
            l, r = -1, 0
            interval = 0
            val, jump = cache.get(r, (10**7, -1))
            if val <= goal:
                interval += val
                r = jump+1
            while l < length and remainDay >= -1:
                while r < length and interval+weights[r] <= goal:
                    interval += weights[r]
                    r += 1
                    val, jump = cache.get(r, (10**7, -1))
                    if interval+val <= goal:
                        interval += val
                        r = jump+1
                if interval != 0:
                    cache[l] = (interval, r-1)
                remainDay -= 1
                l = r
                interval = 0

            if remainDay >= 0:
                return goal
            goal += 1