
import csv

def calculate_average(csv_file, column_name):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        total = 0
        count = 0
        for row in reader:
            total += float(row[column_name])
            count += 1
    return total / count

if __name__ == "__main__":
    csv_file = "data.csv"
    column_name = "value"
    
    average_value = calculate_average(csv_file, column_name)
    print(f"The average value in the column '{column_name}' is: {average_value}")
