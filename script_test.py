
def reverse_matrix(matrix):
    reversed_matrix = []
    
    for i in range(len(matrix[0])):
        reversed_row = [matrix[j][i] for j in range(len(matrix))]
        reversed_matrix.append(reversed_row)
    
    return reversed_matrix

# Test the program
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix(matrix)

for row in reversed_matrix:
    print(row)
