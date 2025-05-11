
import csv

def analyze_data(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        data = []
        for row in reader:
            data.append(row)
    
    print("Headers:", headers)
    
    # Analyze the data
    total_rows = len(data)
    total_columns = len(headers)
    
    print("Total rows:", total_rows)
    print("Total columns:", total_columns)
    
    # Example: Calculate average value in the second column
    column_index = 1
    column_values = [float(row[column_index]) for row in data]
    average_value = sum(column_values) / len(column_values)
    
    print("Average value in column {}: {:.2f}".format(column_index, average_value))

# Uncomment and replace 'data.csv' with your CSV file name to use this program
# analyze_data('data.csv')
