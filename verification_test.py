
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if the matrix is a square matrix
    if n != len(matrix[0]):
        return False
    
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    anti_diag_sum = sum(matrix[i][n-i-1] for i in range(n))
    
    if len(set(row_sums)) != 1 or len(set(col_sums)) != 1 or main_diag_sum != row_sums[0] or anti_diag_sum != row_sums[0]:
        return False
    
    magic_sum = row_sums[0]
    
    torus = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 1 or matrix[i][j] > n*n:
                torus = False
                break
    
    return torus

# Test the function
matrix = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

print(is_magic_torus(matrix))  # Output: True
