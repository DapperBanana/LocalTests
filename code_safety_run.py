
def is_magic_torus(matrix):
    n = len(matrix)
    magic_num = sum(matrix[0])  # Calculate magic number

    # Check rows
    for row in matrix:
        if sum(row) != magic_num:
            return False
    
    # Check columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_num:
            return False
    
    # Check diagonals
    diagonal1 = sum(matrix[i][i] for i in range(n))
    diagonal2 = sum(matrix[i][n-1-i] for i in range(n))
    if diagonal1 != magic_num or diagonal2 != magic_num:
        return False

    return True

# Test the program with a sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_torus(matrix):
    print("The matrix is a magic torus.")
else:
    print("The matrix is not a magic torus.")
