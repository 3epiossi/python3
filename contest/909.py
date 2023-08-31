class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        sq = n**2
        r, c = n-1, 0
        alt = 0
        flatten = []
        while r >= 0:
            if alt%2 == 0:
                if c < n:
                    flatten.append( (r,c) )
                    c += 1
                else:
                    c -= 1
                    if r-1 >= 0:
                        r -= 1
                        alt += 1
                    else:
                        break
            else:
                if c >= 0:
                    flatten.append( (r,c) )   
                    c -= 1
                else:
                    c += 1
                    if r-1 >= 0:
                        r -= 1
                        alt += 1
                    else:
                        break

        adj = collections.defaultdict(set)
        for i in range(sq):
            son = i+1
            while son < sq and son <= i+6:
                r, c = flatten[son]
                if board[r][c] == -1:
                    addSon = son
                else:
                    addSon = board[r][c]-1
                adj[i].add(addSon)
                son += 1

        pas = set()
        que = set([0])
        nextQue = set()
        step = 0
        while True:
            for cur in que:
                if cur in pas:
                    continue
                pas.add(cur)
                nextQue.update(adj[cur])
            que.clear()
            que.update(nextQue)
            nextQue.clear()
            step += 1
            if sq-1 in que:
                return step
            if que == set():
                return -1