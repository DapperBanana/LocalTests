
import csv

def calculate_average(csv_file, column_name):
    total = 0
    count = 0

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row[column_name])
            count += 1

    if count == 0:
        return 0
    else:
        return total / count

if __name__ == "__main__":
    file_name = "data.csv"
    column_name = "value"

    average_value = calculate_average(file_name, column_name)
    print(f"The average value of column {column_name} is: {average_value}")
