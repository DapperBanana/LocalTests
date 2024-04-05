
def reverse_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    reversed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            reversed_matrix[j][i] = matrix[i][j]
    
    return reversed_matrix

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix(matrix)
for row in reversed_matrix:
    print(row)
