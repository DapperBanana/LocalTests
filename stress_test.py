
def is_valid_sudoku(board):
    # Check rows
    for i in range(9):
        row_set = set()
        for j in range(9):
            if board[i][j] in row_set:
                return False
            if board[i][j] != '.':
                row_set.add(board[i][j])
    
    # Check columns
    for j in range(9):
        col_set = set()
        for i in range(9):
            if board[i][j] in col_set:
                return False
            if board[i][j] != '.':
                col_set.add(board[i][j])
    
    # Check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_set = set()
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] in subgrid_set:
                        return False
                    if board[i+k][j+l] != '.':
                        subgrid_set.add(board[i+k][j+l])
    
    return True

# Example Sudoku solution
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
    print("This Sudoku solution is valid.")
else:
    print("This Sudoku solution is invalid.")
