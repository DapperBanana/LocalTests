
import csv

with open('data.csv', 'r') as file:
    data = csv.reader(file)
    header = next(data)  # Skip header row
    total = 0
    count = 0

    for row in data:
        value = float(row[0])
        total += value
        count += 1

    if count > 0:
        average = total / count
        print(f'The average value in the first column is: {average}')
    else:
        print('No data found in the CSV file.')
