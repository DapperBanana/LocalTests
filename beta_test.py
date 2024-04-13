
import csv

# Function to read data from CSV file
def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Function to analyze data
def analyze_data(data):
    num_rows = len(data)
    num_columns = len(data[0])
    total_sum = 0
    for row in data:
        for value in row:
            total_sum += int(value)
    
    avg_value = total_sum / (num_rows * num_columns)
    
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")
    print(f"Total sum of values: {total_sum}")
    print(f"Average value: {avg_value}")

# Main program
file_name = 'data.csv'
data = read_csv_file(file_name)
analyze_data(data)
