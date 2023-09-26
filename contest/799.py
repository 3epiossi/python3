class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for cur in range(query_row):
            
            nextRow = [0 for i in range(cur+1+1)]
            for j in range(cur+1):
                nextRow[j] += 0 if row[j] <= 1 else (row[j]-1)/2
                nextRow[j+1] += 0 if row[j] <= 1 else (row[j]-1)/2
            row = nextRow
        return 1 if row[query_glass] > 1 else row[query_glass] 