
import matplotlib.pyplot as plt

# Dictionary of data
data = {
    'Apples': 10,
    'Oranges': 8,
    'Bananas': 15,
    'Grapes': 6,
    'Pineapple': 12
}

# Create bar chart
plt.bar(data.keys(), data.values())
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')
plt.show()
