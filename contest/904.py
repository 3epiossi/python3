class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        length = len(fruits)
        if len(set(fruits)) <= 2:
            return length
        def findOthers(cur):
            l, r = cur-1, cur+1
            while l >= 0 and fruits[l] == fruits[cur]:
                l -= 1
            while r < length and fruits[r] == fruits[cur]:
                r += 1
            return (l,r)
        cur = 0
        maxFruits = 0
        while cur < length:
            standardL, standardR = findOthers(cur)
            l, r = standardL, standardR
            if l < 0:
                fruitCur, fruitR = fruits[cur], fruits[r]
                while r < length and fruits[r] in {fruitR, fruitCur}:
                    r += 1
                cur = standardR
                if maxFruits < r-standardL-1:
                    maxFruits = r-standardL-1
                continue
            if r >= length:
                fruitL, fruitCur = fruits[l], fruits[cur]
                while l >= 0 and fruits[l] in {fruitL, fruitCur}:
                    l -= 1
                cur = standardR
                if maxFruits < standardR-l-1:
                    maxFruits = standardR-l-1
                continue
            fruitL, fruitR, fruitCur= fruits[l], fruits[r], fruits[cur]
            while l >= 0 and fruits[l] in {fruitL, fruitCur}:
                l -= 1
            while r < length and fruits[r] in {fruitR, fruitCur}:
                r += 1
            cur = standardR
            if maxFruits < standardR-l-1:
                maxFruits = standardR-l-1
            if maxFruits < r-standardL-1:
                maxFruits = r-standardL-1

            
        return maxFruits