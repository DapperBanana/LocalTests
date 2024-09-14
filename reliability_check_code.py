
def reverse_matrix(matrix):
    reversed_matrix = [list(row[::-1]) for row in matrix[::-1]]
    return reversed_matrix

# Example matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

reversed_matrix = reverse_matrix(matrix)

for row in reversed_matrix:
    print(row)
