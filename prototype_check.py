
def is_magic_torus(matrix):
    row_sum = sum(matrix[0])
    col_sum = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
    diagonal_sum1 = sum(matrix[i][i] for i in range(len(matrix)))
    diagonal_sum2 = sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))

    if len(set(row_sum)) == 1 and len(set(col_sum)) == 1 and sum(row_sum) == diagonal_sum1 == diagonal_sum2:
        return True
    else:
        return False

# Example matrix
matrix = [[4, 9, 2],
          [3, 5, 7],
          [8, 1, 6]]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
