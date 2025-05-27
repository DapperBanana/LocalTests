
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    col_sum = sum(matrix[0])
    
    # Check the sum of each row
    for row in matrix:
        if sum(row) != col_sum:
            return False

    # Check the sum of each column
    for i in range(n):
        if sum(matrix[j][i] for j in range(n)) != col_sum:
            return False

    # Check the sum of the main diagonal
    if sum(matrix[i][i] for i in range(n)) != col_sum:
        return False

    # Check the sum of the other diagonal
    if sum(matrix[i][n-i-1] for i in range(n)) != col_sum:
        return False

    return True

# Test the function with a sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
