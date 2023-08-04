class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        iterate = []
        for i in range(m):
            for j in range(n):
                heapq.heappush(iterate, (-heights[i][j], i, j))
        both = set()
        def dfs(row, col, pas):
            if (row, col) in both:
                return 2
            result = set()
            pas.add((row, col))
            if row+1 == m:
                result.add(4)
            elif heights[row][col] >= heights[row+1][col] \
            and (row+1, col) not in pas:
                result.add(dfs(row+1, col, pas))
            if col+1 == n:
                result.add(4)
            elif heights[row][col] >= heights[row][col+1] \
            and (row, col+1) not in pas:
                result.add(dfs(row, col+1, pas))
            if row-1 == -1:
                result.add(9)
            elif heights[row][col] >= heights[row-1][col] \
            and (row-1, col) not in pas:
                result.add(dfs(row-1, col, pas))
            if col-1 == -1:
                result.add(9)
            elif heights[row][col] >= heights[row][col-1] \
            and (row, col-1) not in pas:
                result.add(dfs(row, col-1, pas))
            if 2 in result or (4 in result and 9 in result):
                both.add((row, col))
                return 2
            elif 4 in result:
                return 4
            elif 9 in result:
                return 9
            else:
                return 0
        while iterate:
            h, row, col = heapq.heappop(iterate)
            dfs(row, col, set())
        return both