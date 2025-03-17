
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the main diagonal
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    
    # Check the sum of the rows
    for row in matrix:
        if sum(row) != main_diagonal_sum:
            return False
    
    # Check the sum of the columns
    for i in range(n):
        if sum(matrix[j][i] for j in range(n)) != main_diagonal_sum:
            return False
    
    # Check the sum of the two diagonals
    if sum(matrix[i][n-i-1] for i in range(n)) != main_diagonal_sum:
        return False
    
    return True

# Test the function with an example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
