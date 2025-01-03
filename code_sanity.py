
def is_magic_square(matrix):
    # Check if the matrix is a square
    n = len(matrix)
    if n != len(matrix[0]):
        return False
    
    # Calculate the magic constant
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
    if sum(matrix[i][i] for i in range(n)) != magic_constant or sum(matrix[i][n-i-1] for i in range(n)) != magic_constant:
        return False
    
    return True

# Test the function
matrix = [[2, 7, 6],
          [9, 5, 1],
          [4, 3, 8]]

if is_magic_square(matrix):
    print("The matrix is a magic square.")
else:
    print("The matrix is not a magic square.")
