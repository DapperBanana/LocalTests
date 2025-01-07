
import matplotlib.pyplot as plt

# Data
data = {
    'January': 100,
    'February': 150,
    'March': 200,
    'April': 180,
    'May': 220,
    'June': 250
}

# Extract x values and y values
months = list(data.keys())
values = list(data.values())

# Create line chart
plt.plot(months, values, marker='o', color='b', linestyle='-')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Simple Line Chart')

# Display the chart
plt.show()
