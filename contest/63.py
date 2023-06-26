class Solution:
    def dfs(self, obstacleGrid, x, y, dtdp):
        if x >= len(obstacleGrid) or y >= len(obstacleGrid[0]) or obstacleGrid[x][y] == 1:
            return 0
        if (x, y) == (len(obstacleGrid)-1, len(obstacleGrid[0])-1):
            return 1
        if (x, y) in dtdp:
            return dtdp[(x, y)]
        ctrt = 0
        ctdw = 0
        ctdw = self.dfs(obstacleGrid, x+1, y, dtdp)
        ctrt = self.dfs(obstacleGrid, x, y+1, dtdp)
        dtdp[(x, y)] = ctrt + ctdw
        return ctrt + ctdw
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ct = 0
        x, y = 0, 0
        dtdp = dict()
        return self.dfs(obstacleGrid, x, y, dtdp)
        