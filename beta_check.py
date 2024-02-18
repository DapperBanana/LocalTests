
def is_magic_square(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    # Check if all rows sum up to the same number
    total_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != total_sum:
            return False

    # Check if all columns sum up to the same number
    for i in range(len(matrix[0])):
        if sum(row[i] for row in matrix) != total_sum:
            return False

    # Check if both diagonals sum up to the same number
    diagonal_sum1 = sum(matrix[i][i] for i in range(len(matrix)))
    diagonal_sum2 = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
    if diagonal_sum1 != total_sum or diagonal_sum2 != total_sum:
        return False

    return True

# Test the function with a sample matrix
matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
if is_magic_square(matrix):
    print("The matrix is a magic square")
else:
    print("The matrix is not a magic square")
