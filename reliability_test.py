
import csv

# Function to read data from CSV file
def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return headers, data

# Function to analyze the data
def analyze_data(headers, data):
    num_records = len(data)
    total = sum([int(row[1]) for row in data])
    average = total / num_records
    max_value = max([int(row[1]) for row in data])
    min_value = min([int(row[1]) for row in data])

    print(f"Number of records: {num_records}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Max value: {max_value}")
    print(f"Min value: {min_value}")

# Main program
if __name__ == '__main__':
    file_name = 'data.csv'
    headers, data = read_csv_file(file_name)
    analyze_data(headers, data)
