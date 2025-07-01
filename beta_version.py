
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
data = pd.read_csv('countries_gdp.csv')

# Extract countries and GDPs from the data
countries = data['Country']
gdps = data['GDP']

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(countries, gdps, color='skyblue')
plt.xlabel('Countries')
plt.ylabel('GDP (in Trillion USD)')
plt.title('GDP of Countries')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
