lass Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        end = flowers[:]
        flowers.sort()
        end.sort(key=lambda x : x[1])
        res = [0 for _ in range(len(people))]
        length = len(flowers)
        for i, t in enumerate(people):
            l, r = 0, length-1
            m = 0
            while l < r:
                m = (l+r)//2
                if flowers[r][0] == t:
                    while r+1 < length and flowers[r+1][0] == t : r += 1 
                    break
                if flowers[m][0] < t:
                    l = m+1
                else:
                    r = m
            res[i] = r if flowers[r][0] <= t else r-1
            l, r = 0, length-1
            while l < r:
                m = (l+r)//2
                if end[l][1] == t:
                    while l > 0 and end[l][1] == t : l -= 1 
                    break
                if end[m][1] < t:
                    l = m+1
                else:
                    r = m
            l = l-1 if t <= end[l][1] else l
            res[i] = res[i]-l
        return res
