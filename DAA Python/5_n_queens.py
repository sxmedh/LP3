# N-Queens Puzzle with Backtracking: Placing the First Queen and Generating the Final Matrix

# Function to print Chessboard
def printSolution(board, x, y):
    print()
    print("N Queen Backtracking Solution: ")
    print(f"Initial Position    (x: {x}, y: {y})")
    print()
    for line in board:
        print(line)

# Function to check if a square is attacked or not
def is_attack(i, j, board, N):
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

# Utility function for solveNQ
def solveNQUtil(board, col, x, y, N):
    if col >= N:
        return True

    if col == y:
        return solveNQUtil(board, col + 1, x, y, N)

    for i in range(N):
        if i == x:
            continue
        if (not (is_attack(i, col, board, N))) and (board[i][col] != 1):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, x, y, N):
                return True
            board[i][col] = 0

    return False

# Function to solve N Queen
def solveNQ():
    N = int(input("Enter the size of the board (N): "))
    x = int(input("Enter the initial row: "))
    y = int(input("Enter the initial column: "))

    board = [[0 for _ in range(N)] for _ in range(N)]
    board[x][y] = 1

    if not solveNQUtil(board, 0, x, y, N):
        print()
        print("Solution does not exist")
        print()
        return False

    printSolution(board, x, y)
    return True

solveNQ()


# ----------------------------------------------------------------------

# OUTPUT- (where solution exists)

# Enter the size of the board (N): 4
# Enter the initial row: 2
# Enter the initial column: 0

# N Queen Backtracking Solution: 
# Initial Position    (x: 2, y: 0)

# [0, 1, 0, 0]
# [0, 0, 0, 1]
# [1, 0, 0, 0]
# [0, 0, 1, 0]

# ----------------------------------------------------------------------

# OUTPUT- (where solution does not exists)

# Enter the size of the board (N): 4
# Enter the initial row: 0
# Enter the initial column: 0

# Solution does not exist  
    



