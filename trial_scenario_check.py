
import pandas as pd

# Read the CSV file
data = pd.read_csv('data.csv')

# Display the first 5 rows of the data
print("First 5 rows:")
print(data.head())

# Display the shape of the data (number of rows and columns)
print("Data shape:")
print(data.shape)

# Display the column names
print("Column names:")
print(data.columns)

# Display summary statistics of the data
print("Summary statistics:")
print(data.describe())

# Calculate the average of a specific column
average_value = data['Column Name'].mean()
print(f"Average value: {average_value}")

# Calculate the maximum value of a specific column
max_value = data['Column Name'].max()
print(f"Maximum value: {max_value}")

# Calculate the minimum value of a specific column
min_value = data['Column Name'].min()
print(f"Minimum value: {min_value}")

# Calculate the total sum of a specific column
total_sum = data['Column Name'].sum()
print(f"Total sum: {total_sum}")
