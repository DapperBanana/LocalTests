
import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return header, data

def analyze_data(header, data):
    num_rows = len(data)
    num_cols = len(header)
    unique_values = set()
    empty_cells = 0
    
    for row in data:
        for value in row:
            if value == "":
                empty_cells += 1
            else:
                unique_values.add(value)
    
    print("Number of Rows:", num_rows)
    print("Number of Columns:", num_cols)
    print("Unique Values:", unique_values)
    print("Empty Cells:", empty_cells)

# Example usage
file_path = "data.csv"
header, data = read_csv(file_path)
analyze_data(header, data)
