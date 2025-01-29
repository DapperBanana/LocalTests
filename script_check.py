
def is_valid_sudoku(board):
    # Check rows
    for i in range(9):
        row = set()
        for j in range(9):
            if board[i][j] in row:
                return False
            if board[i][j] != '.':
                row.add(board[i][j])
    
    # Check columns
    for j in range(9):
        col = set()
        for i in range(9):
            if board[i][j] in col:
                return False
            if board[i][j] != '.':
                col.add(board[i][j])
    
    # Check subgrids
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            subgrid = set()
            for i in range(k, k+3):
                for j in range(l, l+3):
                    if board[i][j] in subgrid:
                        return False
                    if board[i][j] != '.':
                        subgrid.add(board[i][j])
                        
    return True

# Example board
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

if is_valid_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
