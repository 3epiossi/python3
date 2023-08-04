class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        pas = set()
        def nei(num):
            possible = []
            res = []
            for c in list(num):
                n = int(c)
                if n == 0:
                    possible.append(('9','1'))
                elif n == 9:
                    possible.append(('8','0'))
                else:
                    a, b = list(map(str,[n-1,n+1]))
                    possible.append((a,b))
            for i in possible[0]:
                new = i+num[1:4]
                if new not in pas and new not in deadends:
                    res.append(new)
            for i in possible[1]:
                new = num[0]+i+num[2:4]
                if new not in pas and new not in deadends:
                    res.append(new)
            for i in possible[2]:
                new = num[0:2]+i+num[3]
                if new not in pas and new not in deadends:
                    res.append(new)
            for i in possible[3]:
                new = num[0:3]+i
                if new not in pas and new not in deadends:
                    res.append(new)
            return res
        que = ['0000']
        step = 0
        nextQue = set()
        while que:
            cur = que.pop(0)
            if cur == target:
                return step
            pas.add(cur)
            nextQue.update(nei(cur))
            if que == []:
                que.extend(nextQue)
                step += 1
                nextQue = set()
        return -1