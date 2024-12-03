
import pandas as pd

# Load the Excel spreadsheet into a DataFrame
df = pd.read_excel('data.xlsx')

# Display the first 5 rows of the DataFrame
print("First 5 rows of the data:")
print(df.head())

# Display the shape of the DataFrame (number of rows and columns)
print("Shape of the data:")
print(df.shape)

# Display the column names of the DataFrame
print("Column names:")
print(df.columns)

# Display summary statistics of the numerical columns
print("Summary statistics:")
print(df.describe())

# Calculate the average value of a specific column
avg_value = df['column_name'].mean()
print("Average value of column 'column_name':", avg_value)

# Perform any other analysis as needed

# Save the analyzed data to a new Excel spreadsheet
df.to_excel('analyzed_data.xlsx', index=False)
