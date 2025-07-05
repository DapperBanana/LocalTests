
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if all rows have the same sum
    row_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != row_sum:
            return False
    
    # Check if all columns have the same sum
    col_sum = sum(matrix[i][0] for i in range(n))
    for i in range(n):
        if sum(matrix[row][i] for row in range(n)) != col_sum:
            return False
    
    # Check if the main diagonal has the same sum
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    if main_diagonal_sum != row_sum:
        return False

    # Check if the secondary diagonal has the same sum
    secondary_diagonal_sum = sum(matrix[i][n-1-i] for i in range(n))
    if secondary_diagonal_sum != row_sum:
        return False
    
    return True

# Example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
