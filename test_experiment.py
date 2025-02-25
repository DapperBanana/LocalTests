
import csv

def analyze_csv_file(csv_file_path):
    data = []
    
    # Read data from CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        
        for row in csv_reader:
            data.append(row)
    
    # Calculate average value of a specific column
    column_to_analyze = 1  # change this to the index of the column you want to analyze
    values = [float(row[column_to_analyze]) for row in data]
    avg_value = sum(values) / len(values)
    
    return avg_value

# Replace 'data.csv' with the path to your CSV file
csv_file_path = 'data.csv'
average_value = analyze_csv_file(csv_file_path)

print(f"The average value of column 1 in the CSV file is: {average_value}")
