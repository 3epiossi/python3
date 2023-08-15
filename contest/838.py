class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        dominoes = list(dominoes)
        res = ""
        l, r = 0, 1
        while l < length:
            while r < length-1 and dominoes[r] not in {'L', 'R'} : r += 1
            if r < length and dominoes[r] == 'L':
                if dominoes[l] == 'R':
                    ll = l
                    rr = r
                    while ll < rr:
                        dominoes[ll] = 'R'
                        dominoes[rr] = 'L'
                        ll += 1
                        rr -= 1
                    
                else:
                    for i in range(l,r+1):
                        dominoes[i] = 'L'
            elif r < length:
                if dominoes[l] == 'R':
                    for i in range(l,r+1):
                        dominoes[i] = 'R'
            l = r
            r = l+1
        return ''.join(dominoes)