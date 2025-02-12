
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    
    # Calculate the sum of the second diagonal
    sum_diag2 = sum(matrix[i][n-i-1] for i in range(n))
    
    if sum_diag1 != sum_diag2:
        return False
    
    # Check rows and columns
    for i in range(n):
        if sum(matrix[i][j] for j in range(n)) != sum_diag1:
            return False
        if sum(matrix[j][i] for j in range(n)) != sum_diag1:
            return False
    
    return True

# Test the program with a sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The matrix is a magic square!")
else:
    print("The matrix is not a magic square.")
