
def is_magic_torus(matrix):
    n = len(matrix)
    magic_number = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != magic_number:
            return False

    # Check columns
    for col in range(n):
        if sum(row[col] for row in matrix) != magic_number:
            return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_number:
        return False

    if sum(matrix[i][n-1-i] for i in range(n)) != magic_number:
        return False

    return True

# Test the program
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus")
else:
    print("The given matrix is not a magic torus")
