
import csv

def analyze_data(file_name):
    with open(file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # read the header row
        header = next(csvreader)
        
        # initialize variables to store data
        data = []
        
        # read data rows
        for row in csvreader:
            data.append(row)
    
    # calculate some basic statistics
    num_rows = len(data)
    num_cols = len(header)
    
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_cols}")
    
    # assuming the data consists of numerical values, calculate average of each column
    averages = []
    for i in range(num_cols):
        col_values = [float(row[i]) for row in data]
        avg = sum(col_values) / len(col_values)
        averages.append(avg)
        print(f"Average of column {header[i]}: {avg}")
    
if __name__ == '__main__':
    file_name = 'data.csv'
    analyze_data(file_name)
