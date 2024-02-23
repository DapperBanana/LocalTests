
def reverse_matrix(matrix):
    reversed_matrix = []
    for i in range(len(matrix[0])):
        reversed_row = []
        for j in range(len(matrix)):
            reversed_row.append(matrix[j][i])
        reversed_matrix.append(reversed_row)
    return reversed_matrix

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reversed_matrix = reverse_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nReversed Matrix:")
for row in reversed_matrix:
    print(row)
