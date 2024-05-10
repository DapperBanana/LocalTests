
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    sum_row = sum(matrix[0])
    
    # Check if the sum of rows is equal to the sum of the first row
    for row in matrix:
        if sum(row) != sum_row:
            return False
    
    # Check if the sum of columns is equal to the sum of the first row
    for j in range(n):
        sum_col = 0
        for i in range(n):
            sum_col += matrix[i][j]
        if sum_col != sum_row:
            return False
    
    # Check if the sum of the main diagonal is equal to the sum of the first row
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    if sum_diag1 != sum_row:
        return False
    
    # Check if the sum of the secondary diagonal is equal to the sum of the first row
    sum_diag2 = sum(matrix[i][n-1-i] for i in range(n))
    if sum_diag2 != sum_row:
        return False
    
    return True

# Test the program
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The matrix is a magic square")
else:
    print("The matrix is not a magic square")
