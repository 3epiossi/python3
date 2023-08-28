lass Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        coeffi = []
        while True:
            if columnNumber <= 26:
                coeffi.append(columnNumber)
                break
            coeffi.append(columnNumber%26)
            columnNumber  = columnNumber//26
        l, r = 0, 0
        while l < len(coeffi):
            if coeffi[l] != 0:
                l += 1
            else:
                r = l+1
                while coeffi[r] == 0:
                    coeffi[r] = 25
                    r += 1
                if r < len(coeffi)-1 or coeffi[r] != 1:
                    coeffi[r] -= 1
                    coeffi[l] = 26
                else:
                    coeffi[l] = 26
                    coeffi.pop()
                l = r
        res = ""
        from string import ascii_uppercase
        for num in coeffi:
            res = ascii_uppercase[num-1] + res
        return res