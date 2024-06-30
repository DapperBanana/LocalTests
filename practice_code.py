
import csv

# Function to read data from CSV file
def read_data(file_name):
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
    total_values = sum([int(value) for row in data for value in row])
    
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")
    print(f"Total sum of all values: {total_values}")

# Main program
if __name__ == "__main__":
    file_name = "data.csv"
    data = read_data(file_name)
    analyze_data(data)
