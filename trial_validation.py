
def check_magic_torus(matrix):
    n = len(matrix)
    magic_number = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != magic_number:
            return False

    # Check columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_number:
            return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_number:
        return False

    if sum(matrix[i][n-i-1] for i in range(n)) != magic_number:
        return False

    return True


# Example usage
matrix = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
is_magic_torus = check_magic_torus(matrix)

if is_magic_torus:
    print("The matrix is a magic torus.")
else:
    print("The matrix is not a magic torus.")
