
def is_valid_sudoku(board):
    N = 9
    
    # Check rows
    for i in range(N):
        if not is_valid_group([board[i][j] for j in range(N)]):
            return False
    
    # Check columns
    for j in range(N):
        if not is_valid_group([board[i][j] for i in range(N)]):
            return False
    
    # Check 3x3 subgrids
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            if not is_valid_group([board[i+m][j+n] for m in range(3) for n in range(3)]):
                return False
    
    return True

def is_valid_group(group):
    seen = set()
    for num in group:
        if num != "." and num in seen:
            return False
        seen.add(num)
    return True

# Test the program with a valid Sudoku solution
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

if is_valid_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
