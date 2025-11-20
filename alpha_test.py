
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if the matrix is a square matrix
    for row in matrix:
        if len(row) != n:
            return False
    
    # Calculate the magic constant
    magic_constant = n * (n**2 + 1) // 2
    
    # Check rows and columns
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        
        if row_sum != magic_constant or col_sum != magic_constant:
            return False
    
    # Check diagonals
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n-1-i] for i in range(n))
    
    if diag1_sum != magic_constant or diag2_sum != magic_constant:
        return False
    
    return True

# Test the function with an example magic torus
matrix = [
    [4, 14, 15, 1],
    [9, 7, 6, 12],
    [5, 11, 10, 8],
    [16, 2, 3, 13]
]

print(is_magic_torus(matrix))  # Output: True
