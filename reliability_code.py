
import csv

# Function to read data from CSV file
def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Function to analyze data
def analyze_data(data):
    num_rows = len(data)
    num_columns = len(data[0])
    total_values = sum([float(value) for row in data for value in row])
    average_value = total_values / (num_rows * num_columns)
    
    print("Number of rows:", num_rows)
    print("Number of columns:", num_columns)
    print("Total values:", total_values)
    print("Average value:", average_value)

# Main program
if __name__ == '__main__':
    filename = 'data.csv'
    data = read_csv_file(filename)
    analyze_data(data)
