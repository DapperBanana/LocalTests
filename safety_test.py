
import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data

def analyze_data(data):
    num_rows = len(data)
    num_cols = len(data[0])
    column_sums = [0] * num_cols
    column_avgs = [0] * num_cols

    for row in data:
        for i in range(num_cols):
            column_sums[i] += int(row[i])

    for i in range(num_cols):
        column_avgs[i] = column_sums[i] / num_rows

    return num_rows, num_cols, column_sums, column_avgs

def main():
    file_path = 'data.csv'  # Replace with your file path
    data = read_csv_file(file_path)
    num_rows, num_cols, column_sums, column_avgs = analyze_data(data)

    print(f'Number of rows: {num_rows}')
    print(f'Number of columns: {num_cols}')
    print('Column sums:', column_sums)
    print('Column averages:', column_avgs)

if __name__ == '__main__':
    main()
