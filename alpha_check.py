
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if it's a square matrix
    if n != len(matrix[0]):
        return False
    
    # Calculate the magic constant
    magic_constant = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    
    # Check columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_constant:
            return False
    
    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_constant:
        return False
    
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_constant:
        return False
    
    return True

# Test the function
matrix = [[2, 7, 6],
          [9, 5, 1],
          [4, 3, 8]]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
