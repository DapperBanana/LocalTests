
def is_magic_square(matrix):
    N = len(matrix)
    
    # Calculate sum of first row
    sum_first_row = sum(matrix[0])

    # Check all rows
    for row in matrix:
        if sum(row) != sum_first_row:
            return False
    
    # Check all columns
    for i in range(N):
        sum_col = sum(matrix[j][i] for j in range(N))
        if sum_col != sum_first_row:
            return False
    
    # Check diagonal
    diag_sum = sum(matrix[i][i] for i in range(N))
    if diag_sum != sum_first_row:
        return False
    
    # Check reverse diagonal
    reverse_diag_sum = sum(matrix[i][N-i-1] for i in range(N))
    if reverse_diag_sum != sum_first_row:
        return False
    
    return True

# Test the function with a sample matrix
matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
