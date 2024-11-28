
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the expected sum of each row, column, and diagonal
    expected_sum = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != expected_sum:
            return False
    
    # Check columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != expected_sum:
            return False
    
    # Check main diagonal
    if sum(matrix[i][i] for i in range(n)) != expected_sum:
        return False
    
    # Check secondary diagonal
    if sum(matrix[i][n-i-1] for i in range(n)) != expected_sum:
        return False
    
    return True

# Example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
