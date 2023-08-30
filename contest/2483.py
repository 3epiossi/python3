class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = 0
        Y = customers.count('Y')
        minTotal = (0,N+Y)
        for i, c in enumerate(customers):
            i += 1
            if c == 'N':
                N += 1
                if N+Y < minTotal[1]:
                    minTotal = (i, N+Y)
            elif c == 'Y':
                Y -= 1
                if N+Y < minTotal[1]:
                    minTotal = (i, N+Y)
        return minTotal[0]