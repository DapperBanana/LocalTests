
def reverse_matrix(matrix):
    reversed_matrix = []
    
    # Reverse the order of rows
    for row in reversed(matrix):
        reversed_row = []
        for item in row:
            reversed_row.append(item)
        reversed_matrix.append(reversed_row)
    
    # Reverse the order of columns
    for i in range(len(reversed_matrix)):
        reversed_matrix[i] = list(reversed(reversed_matrix[i]))
    
    return reversed_matrix

# Test the function with a sample 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix(matrix)

for row in reversed_matrix:
    print(row)
