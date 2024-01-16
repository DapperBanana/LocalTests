
import csv

def read_csv(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

# Replace "data.csv" with the path to your CSV file
read_csv('data.csv')
