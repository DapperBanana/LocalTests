
import csv

def read_csv_file(filepath):
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            print(row)

# Specify the file path of the CSV file
file_path = 'example.csv'

# Call the function
read_csv_file(file_path)
