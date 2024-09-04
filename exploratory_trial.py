
import pandas as pd

# Read the Excel file
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the data
print(data.head())

# Analyze the data
summary = data.describe()
print(summary)

# Calculate the mean of a specific column
column_name = 'Column1'
mean_value = data[column_name].mean()
print(f"The mean of {column_name} is: {mean_value}")
