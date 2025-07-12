
def is_magic_torus(matrix):
    n = len(matrix)
    target_sum = n * (n**2 + 1) / 2
  
    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False
  
    # Check columns
    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != target_sum:
            return False
  
    # Check diagonals
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n-1-i] for i in range(n))
  
    if diag1_sum != target_sum or diag2_sum != target_sum:
        return False
    
    return True

# Test the program
matrix = [
    [1, 14, 14, 4],
    [11, 7, 6, 9],
    [8, 10, 10, 5],
    [13, 2, 3, 15]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus")
else:
    print("The given matrix is not a magic torus")
