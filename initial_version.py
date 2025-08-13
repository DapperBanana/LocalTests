
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check rows
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False
    
    # Check columns
    col_sums = [sum(col) for col in zip(*matrix)]
    if len(set(col_sums)) != 1:
        return False
    
    # Check diagonals
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n-i-1] for i in range(n))
    if diag1_sum != diag2_sum or diag1_sum != row_sums[0]:
        return False
    
    return True

# Test the program
matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(is_magic_torus(matrix))  # True

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(is_magic_torus(matrix))  # False
