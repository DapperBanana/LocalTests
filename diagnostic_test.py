
import csv

def print_csv_file(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))

# Replace 'file.csv' with the path to your CSV file
print_csv_file('file.csv')
