
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False
    
    # Check subgrids
    for i in range(3):
        for j in range(3):
            subgrid = [board[sub_i][sub_j] for sub_i in range(3*i, 3*i+3) for sub_j in range(3*j, 3*j+3)]
            if not is_valid_set(subgrid):
                return False
    
    return True

def is_valid_set(nums):
    seen = set()
    for num in nums:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True

# Sample Sudoku board
board = [
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ['3', '4', '5', '2', '8', '6', '1', '7', '9']
]

if is_valid_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
