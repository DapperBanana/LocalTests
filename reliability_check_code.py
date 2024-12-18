
def is_magic_torus(matrix):
    n = len(matrix)
    magic_num = n * (n*n + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_num:
            return False
    
    # Check columns
    for i in range(n):
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != magic_num:
            return False
    
    # Check diagonals
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][-i-1] for i in range(n))
    
    if diag1_sum != magic_num or diag2_sum != magic_num:
        return False
    
    return True

# Test the function
matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if is_magic_torus(matrix):
    print("The matrix is a magic torus!")
else:
    print("The matrix is not a magic torus.")
