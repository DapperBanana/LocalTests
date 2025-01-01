
import csv

# Function to read data from CSV file
def read_data_from_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Function to analyze data
def analyze_data(data):
    num_rows = len(data)
    num_columns = len(data[0])
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")

# Main program
if __name__ == "__main__":
    file_path = "data.csv"
    data = read_data_from_csv(file_path)
    analyze_data(data)
