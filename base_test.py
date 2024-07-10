
def reverse_matrix(matrix):
    reversed_matrix = [list(row) for row in zip(*matrix[::-1])]
    return reversed_matrix

# Test the function with an example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix(matrix)

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Print the reversed matrix
print("\nReversed Matrix:")
for row in reversed_matrix:
    print(row)
