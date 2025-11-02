
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Calculate the magic sum
    magic_sum = sum(matrix[0])
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    
    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_sum:
        return False
    
    return True

# Test the program
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
