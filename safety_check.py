
import pandas as pd

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Display the first few rows of the dataframe
print("First few rows of the dataframe:")
print(df.head())

# Calculate some statistics on a specific column
column_name = 'column_name_to_analyze'
mean_value = df[column_name].mean()
median_value = df[column_name].median()
max_value = df[column_name].max()
min_value = df[column_name].min()

# Display the calculated statistics
print(f"Mean value of {column_name}: {mean_value}")
print(f"Median value of {column_name}: {median_value}")
print(f"Maximum value of {column_name}: {max_value}")
print(f"Minimum value of {column_name}: {min_value}")
