class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        min = 101
        def dfs(stones):
            nonlocal min
            length = len(stones)
            if length == 1 :
                if stones[0] < min:
                    min = stones[0]
                return min
            if length == 0:
                min = 0
                return 0
            for ix1 in range(length-1):
                for ix2 in range(ix1+1, length):
                    smash = abs(stones[ix1]-stones[ix2])
                    if  smash != 0:
                        try:
                            if dfs(stones[:ix1]+stones[ix1+1:ix2]+stones[ix2+1:]+[smash]) == 0:
                                return 0
                        except:
                            if dfs(stones[:ix1]+stones[ix1+1:ix2]+[smash]) == 0:
                                return 0

                    else:
                        try:
                            if dfs(stones[:ix1]+stones[ix1+1:ix2]+stones[ix2+1:]) == 0:
                                return 0
                        except:
                            if dfs(stones[:ix1]+stones[ix1+1:ix2]) == 0:
                                return 0
        dfs(stones)
        return min