
def validate_sudoku(board):
    # Check rows
    for i in range(9):
        row = set()
        for j in range(9):
            if board[i][j] in row:
                return False
            row.add(board[i][j])
    
    # Check columns
    for j in range(9):
        col = set()
        for i in range(9):
            if board[i][j] in col:
                return False
            col.add(board[i][j])
    
    # Check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if board[x][y] in subgrid:
                        return False
                    subgrid.add(board[x][y])
    
    return True

# Example Sudoku solution
board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if validate_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
