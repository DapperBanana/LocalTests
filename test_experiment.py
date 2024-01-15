
def is_magic_torus(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check columns
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != magic_sum:
            return False
    
    # Check diagonals
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    anti_diag_sum = sum(matrix[i][n-i-1] for i in range(n))
    if main_diag_sum != magic_sum or anti_diag_sum != magic_sum:
        return False
    
    return True


# Test the program
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(is_magic_torus(matrix))  # Output: True

matrix = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 6, 12],
    [4, 14, 15, 1]
]
print(is_magic_torus(matrix))  # Output: True

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(is_magic_torus(matrix))  # Output: False
