
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if the rows, columns, and diagonals all have the same sum
    magic_sum = sum(matrix[0])
    
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    for i in range(n):
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != magic_sum:
            return False
    
    diagonal_sum1 = sum(matrix[i][i] for i in range(n))
    diagonal_sum2 = sum(matrix[i][n-1-i] for i in range(n))
    
    if diagonal_sum1 != magic_sum or diagonal_sum2 != magic_sum:
        return False
    
    return True

# Test the program with a sample matrix
matrix = [[2, 7, 6],
          [9, 5, 1],
          [4, 3, 8]]

if is_magic_torus(matrix):
    print("The matrix is a magic torus!")
else:
    print("The matrix is not a magic torus.")
