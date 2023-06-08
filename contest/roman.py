class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        dtone = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        dttwo = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        l, r = 0, 0
        while True:
            if l >= len(s):
                break
            r = l
            while True:
                try:
                    s[r]
                except:
                    break
                if s[l:r+1] in dttwo:
                    break
                if s[r] != s[l]:
                    break
                r += 1 
            if s[l:r+1] in dttwo:
                res += dttwo[s[l:r+1]]
                l = r+1
                continue
            else:
                res += dtone[s[l]]*len(s[l:r])
                l = r
                continue
        return res