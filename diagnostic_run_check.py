
import csv

def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))

# Specify the CSV file name
file_name = 'data.csv'

# Read and print the contents of the CSV file
read_csv_file(file_name)
