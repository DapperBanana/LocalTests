
def reverse_matrix(matrix):
    # Reverse the order of rows
    reversed_matrix = matrix[::-1]
    
    # Reverse the order of columns by transposing the matrix
    reversed_matrix = list(zip(*reversed_matrix))
    
    return reversed_matrix

# Testing the program
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

reversed_matrix = reverse_matrix(matrix)

# Print the reversed matrix
for row in reversed_matrix:
    print(row)
