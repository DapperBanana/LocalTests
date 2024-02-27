
import csv

filename = 'data.csv'

with open(filename, 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
