
import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('data.xlsx')

# Print the first 5 rows of the DataFrame
print("First 5 rows of the data:")
print(df.head())

# Print the shape of the DataFrame (number of rows and columns)
print("\nShape of the data:")
print(df.shape)

# Print some basic statistics of the data
print("\nBasic statistics of the data:")
print(df.describe())

# Calculate and print the average value of a specific column
print("\nAverage value of Column A:", df['Column A'].mean())

# Calculate and print the total sum of a specific column
print("\nTotal sum of Column B:", df['Column B'].sum())

# Count and print the number of unique values in a specific column
print("\nNumber of unique values in Column C:", len(df['Column C'].unique()))

# Group the data by a specific column and calculate the mean of another column
grouped_df = df.groupby('Column D')['Column E'].mean()
print("\nMean value of Column E grouped by Column D:")
print(grouped_df)
