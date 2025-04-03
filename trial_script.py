
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if the matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        return False
    
    magic_constant = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    
    # Check columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_constant:
            return False
    
    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_constant:
        return False
    
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_constant:
        return False
    
    return True

# Test the function
matrix = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

print(is_magic_torus(matrix))  # Output: True
