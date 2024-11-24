
def is_magic_torus(matrix):
    # Check if the matrix is a square matrix
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    
    # Calculate the target sum for rows, columns, and diagonals
    target_sum = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Check columns
    for i in range(n):
        col_sum = sum(row[i] for row in matrix)
        if col_sum != target_sum:
            return False
    
    # Check diagonals
    diagonal_sum_1 = sum(matrix[i][i] for i in range(n))
    diagonal_sum_2 = sum(matrix[i][n-i-1] for i in range(n))
    if diagonal_sum_1 != target_sum or diagonal_sum_2 != target_sum:
        return False
    
    return True

# Test the program
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

print(is_magic_torus(matrix))  # Output: True
