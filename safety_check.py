
import csv

# Function to read data from CSV file
def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Function to analyze data
def analyze_data(data):
    num_rows = len(data)
    num_columns = len(data[0])
    print("Number of rows:", num_rows)
    print("Number of columns:", num_columns)
    
    # Calculate average value for each column
    averages = []
    for i in range(num_columns):
        column_values = [float(row[i]) for row in data[1:]] # Exclude header row
        average = sum(column_values) / len(column_values)
        averages.append(average)
        print(f"Average value for column {i+1}: {average:.2f}")
    
    # Calculate total sum for each column
    totals = []
    for i in range(num_columns):
        column_values = [float(row[i]) for row in data[1:]] # Exclude header row
        total = sum(column_values)
        totals.append(total)
        print(f"Total sum for column {i+1}: {total:.2f}")
    
# Main function
if __name__ == "__main__":
    filename = "data.csv"
    data = read_data(filename)
    
    if len(data) == 0:
        print("No data found in the CSV file.")
    else:
        analyze_data(data)
