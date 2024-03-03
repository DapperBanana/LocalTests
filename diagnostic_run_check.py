
import matplotlib.pyplot as plt

# Sample data dictionary
data = {'January': 100, 'February': 150, 'March': 200, 'April': 180, 'May': 220}

# Extract x and y values from the data dictionary
months = list(data.keys())
values = list(data.values())

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot(months, values, marker='o', color='skyblue', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()
