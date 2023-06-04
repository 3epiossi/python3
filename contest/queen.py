# A function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # If none of the above conditions are true, it is safe to place a queen
    return True

# A recursive function to solve N Queen problem
def solve_n_queens(board, col):
    # Base case: If all queens are placed then print the solution
    if col == N:
        print_solution(board)
        return True
    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(N):
        # Check if queen can be placed on board[i][col]
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            # Make result true if any placement is possible
            res = solve_n_queens(board, col + 1) or res
            # Backtrack: Remove queen from board[i][col]
            board[i][col] = 0
    # If queen can not be placed in any row in this column col then return false
    return res

# A function to print the solution
def print_solution(board):
    global count
    count += 1
    print(f"Solution {count}:")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

# Driver code
N = 8 # Number of queens
board = [[0 for j in range(N)] for i in range(N)] # Initialize an empty board
count = 0 # Initialize a counter for solutions
solve_n_queens(board, 0) # Call the function with the first column as argument

