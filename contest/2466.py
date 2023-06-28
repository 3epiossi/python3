class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ctret = 0
        for length in range(low, high+1):
            zerolen = 0
            onelen = length 
            while onelen >= 0 :
                if zerolen%zero == 0 and onelen%one == 0:
                    ctret += (math.factorial(zerolen//zero + onelen//one)//math.factorial(zerolen//zero)//math.factorial(onelen//one))%(10**9+7)
                    pass 
                zerolen += 1
                onelen -= 1
                pass
            pass

        return ctret % (10**9 + 7)