
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        seen = set()
        for num in row:
            if num != ".":
                if num in seen:
                    return False
                seen.add(num)
    
    # Check columns
    for col in range(9):
        seen = set()
        for row in range(9):
            num = board[row][col]
            if num != ".":
                if num in seen:
                    return False
                seen.add(num)
    
    # Check 3x3 grids
    for i in range(3):
        for j in range(3):
            seen = set()
            for row in range(3*i, 3*i+3):
                for col in range(3*j, 3*j+3):
                    num = board[row][col]
                    if num != ".":
                        if num in seen:
                            return False
                        seen.add(num)
    
    return True

# Test the program
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

print(is_valid_sudoku(board))  # Expect True

board2 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","7"]
]

print(is_valid_sudoku(board2))  # Expect False
