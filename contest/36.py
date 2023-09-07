class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import string
        data = set()
        reData = set()
        block = [ [set() for j in range(3)] for i in range(3)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] in data and board[i][j] in string.digits:
                    return False
                else:
                    data.add(board[i][j])

                
                if board[j][i] in reData and board[j][i] in string.digits:
                    return False
                else:
                    reData.add(board[j][i])

                
                if (board[i][j] in block[i//3][j//3] and
                    board[i][j] in string.digits):
                    return False
                else: ###
                    block[i//3][j//3].add(board[i][j])

                
            data.clear()
            reData.clear()
        return True