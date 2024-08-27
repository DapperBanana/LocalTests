
def reverse_matrix(matrix):
    return [list(row)[::-1] for row in matrix[::-1]]

# Example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reversed_matrix = reverse_matrix(matrix)

for row in reversed_matrix:
    print(row)
